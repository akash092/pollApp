from django import forms

MAX_CHOICES = 5

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=200, label='Your Question')
    pub_date = forms.DateTimeField(label='When to publish?', required=False, widget=forms.TextInput(
            attrs={
                'placeholder': '2006-10-25 14:30:59'
            }
        ))
    created_by = forms.CharField(max_length=200, label='Your Name')
    choice1 = forms.CharField(max_length=200, label='Choice 1')
    choice2 = forms.CharField(max_length=200, label='Choice 2', required=True)
    choice3 = forms.CharField(max_length=200, label='Choice 3', required=False)
    choice4 = forms.CharField(max_length=200, label='Choice 4', required=False)
    choice5 = forms.CharField(max_length=200, label='Choice 5', required=False)