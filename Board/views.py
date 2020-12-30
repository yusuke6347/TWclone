from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.urls import reverse_lazy
from .forms import RegistrationForm, UpdateProfile, CreateTweet
#from django.contrib.auth import login as auth_login
from .models import Tweet, Follow, TWuser
# Create your views here.

class LoginView(AuthLoginView):
    template_name = 'login.html'
    form_class = RegistrationForm

class LogoutView(AuthLogoutView):
    template_name ='logout.html'

class AllListView(generic.ListView):
    template_name = 'all_list.html'
    model = Tweet
    def get_queryset(self):
        return Tweet.objects.order_by('-pub_date')
    

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
            # 'TWuser': user,
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
            'TWuser': user,
        }
        return render(self.request,self.template_name,context)

class UpdateProfileView(generic.UpdateView):
    template_name = 'profile.html'
    model = TWuser
    form_class = UpdateProfile
    success_url = reverse_lazy('home')

class OtherListView(generic.TemplateView):
    template_name='other.html'
    def get(self,request,*args, **kwargs):
        username_k = kwargs["username"]
        user = TWuser.objects.get(username=username_k)
        #Q = Tweet.objects.filter(author__username=user)
        if user == self.request.user:
            return redirect('home')
        is_follow = Follow.objects.filter(follow_user=user,self_user=self.request.user).exists()
        is_follower = Follow.objects.filter(follow_user=self.request.user,self_user=user).exists()
        Q = Tweet.objects.filter(author=user)
        context = {
            'object_list': Q.order_by('-pub_date'),
            'TWuser': user,
            'isFollow': is_follow,
            'isFollower': is_follower,
        }
        return render(self.request,self.template_name,context)
    # def post(self,request,*args,**kwargs):
    #     username_k = kwargs["username"]
    #     user = TWuser.objects.get(username=username_k)
    #     if 'follow' in request.POST:
    #         Follow.objects.create(self_user=self.request.user,follow_user=user)
    #         return redirect('home')
    #     if 'delete-follow' in request.POST:
    #         Follow.objects.filter(follow_user=user,self_user=self.request.user).delete()
    #         return redirect('home')

def create_follow(request,follow_username):
    user = TWuser.objects.get(username=follow_username)
    Follow.objects.create(self_user=request.user,follow_user=user)
    return redirect('other',follow_username)

def delete_follow(request,follow_username):
    user = TWuser.objects.get(username=follow_username)
    Follow.objects.filter(follow_user=user,self_user=request.user).delete()
    return redirect('home')

class CreateTweetView(generic.CreateView):
    template_name='tweet.html'
    form_class=CreateTweet
    success_url=reverse_lazy('home')
    def get_initial(self):
        initial = super().get_initial()
        initial["author"] = self.request.user
        return initial