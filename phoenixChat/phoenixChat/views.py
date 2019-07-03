from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DetailView, ListView

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .forms import SignUpForms, LoginForms

from django.views import generic
from django.views.generic import View
from django.shortcuts import render as render_to_response
from django.template import RequestContext

def signup(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForms()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForms(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = LoginForms()
    return render(request,'login.html',{'form':form})

def home(request):
    users = User.objects.values()
    return render(request, 'home.html', {'users':users})