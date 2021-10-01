from .models import Question, Choice
from .forms import MAX_CHOICES
from django.utils import timezone


# Validates input and make DB calls
# returns True or False indicating success or failure and reason for failure if present
def create(form):
    # check whether user inputted form is valid:
    # https://docs.djangoproject.com/en/3.2/ref/forms/api/#django.forms.Form.is_valid
    if form.is_valid():
        question = Question()
        # process the data in form.cleaned_data as required
        question.question_text = form.cleaned_data['question']
        question.created_by = form.cleaned_data['created_by']
        question.pub_date = form.cleaned_data['pub_date']

        # save the question
        question.before_create()
        question.save()

        # save the choices
        for num in range(1, MAX_CHOICES + 1):
            if form.cleaned_data['choice' + str(num)] is not '':
                choice = Choice()
                choice.question = question
                choice.choice_text = form.cleaned_data['choice' + str(num)]
                choice.save()
        return True, None
    return False, form.errors


def get_all():
    questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return questions


def get_by_id(qid):
    question = Question.objects.get(pk=qid)
    return question


def vote(qid, cid):
    question = get_by_id(qid)  # get the question object
    try:
        choice = question.choice_set.get(pk=cid)  # fetch choice from DB
    except (KeyError, Choice.DoesNotExist):
        # Choice object doesnt exist so error out
        return False, "You didn't select a valid choice."
    else:
        # Choice object is found, increment the counter
        choice.votes += 1
        choice.save()
    return True, ""
