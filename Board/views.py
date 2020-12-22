from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import RegistrationForm
#from django.contrib.auth import login as auth_login
from .models import Tweet
# Create your views here.

class LoginView(AuthLoginView):
    template_name = 'login.html'
    form_class = RegistrationForm

class ListView(generic.ListView):
    template_name = 'list.html'
    model = Tweet

class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Tweet