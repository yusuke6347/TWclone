from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=280)
    photo = models.ImageField(upload_to='',blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content

# class Follow(models.Model):
#     self_id = models.ForeignKey(User.pk,on_delete=models.CASCADE)
#     follow_id = models.ForeignKey(User.pk,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.self_id