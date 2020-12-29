from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TWuser(AbstractUser):
    #prime = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=True)
    icon = models.ImageField(blank=True)
    headerpic = models.ImageField(blank=True)
    def __str__(self):
        return self.username

class Tweet(models.Model):
    content = models.TextField(max_length=280)
    photo = models.ImageField(blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(TWuser,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content

class Follow(models.Model):
    self_user = models.ForeignKey(TWuser,on_delete=models.CASCADE,related_name="su")
    follow_user = models.ForeignKey(TWuser,on_delete=models.CASCADE,related_name="fu")
