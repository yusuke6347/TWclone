from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Tweet, TWuser, Follow

class RegistrationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password 再度確認用'}))
    name = forms.CharField(widget=TextInput(attrs={'placeholder':'アカウント名'}))
    class Meta:
        model = TWuser
        fields = ('username','password1','password2','name')


class CreateTweet(forms.ModelForm):

    class Meta:
        model = Tweet
        exclude = ('pub_date','likes',)
        widgets = {'author': forms.HiddenInput()}


class UpdateProfile(forms.ModelForm):

    class Meta:
        model = TWuser
        fields = ('name','icon')


# class CreateOrDeleteFollow(forms.ModelForm):

#     class Meta:
#         model = Follow
#         fields = '__all__'