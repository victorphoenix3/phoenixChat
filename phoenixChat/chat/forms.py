from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )

