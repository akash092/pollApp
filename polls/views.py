from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import QuestionForm
from . import biz


def index(request):
    latest_question_list = biz.get_all()
    # set parameters needed by HTML page
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        is_success, err_msg = biz.create(form)
        if is_success:
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            # Create black form and show error message
            context = {
                'form': QuestionForm(),
                'error_message': str(err_msg)
            }
    else:
        # if a GET (or any other method) we'll create a blank form
        context = {
            'form': QuestionForm()
        }
    return render(request, 'polls/create.html', context)


def detail(request):
    question_id = request.GET.get('qid')
    question = biz.get_by_id(question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request):
    question_id = request.GET.get('qid')
    question = biz.get_by_id(question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request):
    question_id = request.GET.get('qid')
    if 'choice' in request.POST:
        choice_id_selected = request.POST['choice']
        is_success, err_msg = biz.vote(question_id, choice_id_selected)
        if is_success:
            return HttpResponseRedirect("%s?qid=%s" % (reverse('polls:results'), question_id))
    else:
        err_msg = 'Please select a choice.'

    return render(request, 'polls/detail.html', {
        'question': biz.get_by_id(question_id),
        'error_message': err_msg,
    })
