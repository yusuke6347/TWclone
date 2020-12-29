from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Tweet, TWuser, Follow

class RegistrationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class CreateTweet(forms.ModelForm):

    class Meta:
        model = Tweet
        exclude = ('pub_date','likes',)

class UpdateProfile(forms.ModelForm):

    class Meta:
        model = TWuser
        fields = ('name','icon')

class CreateOrDeleteFollow(forms.ModelForm):

    class Meta:
        model = Follow
        fields = '__all__'