from cProfile import label
import email
import imp
from logging import PlaceHolder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#Sign Up View Function
class SignUpForm(UserCreationForm):

    password2 = forms.CharField(label="Confirm Password(again)", widget = forms.PasswordInput)
    email = forms.CharField(label="Email", widget = forms.EmailInput, required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','is_staff','is_superuser']
        labels = {'username':'Username'}