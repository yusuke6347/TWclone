from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import RegistrationForm
#from django.contrib.auth import login as auth_login
from .models import Tweet, Follow
# Create your views here.

class LoginView(AuthLoginView):
    template_name = 'login.html'
    form_class = RegistrationForm

class ListView(generic.TemplateView):
    template_name = 'list.html'
    def get(self,request,*args, **kwargs):
        user = self.request.user
        Q = Follow.objects.filter(self_user=user)
        follow_list=[]
        for data in Q:
            follow_list.append(data.follow_user)
        follow_list.append(user)
        Tweetset = Tweet.objects.filter(author__in=follow_list)
        context = {
            'object_list':Tweetset.order_by('-pub_date'),
        }
        return render(self.request,self.template_name,context)

class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Tweet

class HomeListView(generic.TemplateView):
    template_name = 'home.html'
    def get(self,request,*args, **kwargs):
        user = self.request.user
        Q = Tweet.objects.filter(author=user)
        context = {
            'object_list': Q.order_by('-pub_date'),
        }
        return render(self.request,self.template_name,context)
