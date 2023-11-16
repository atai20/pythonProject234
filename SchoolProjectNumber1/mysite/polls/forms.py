from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Question

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user']