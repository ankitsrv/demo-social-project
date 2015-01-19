from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
#from django.contrib import admin
#from django.core.mail import send_mail


# Models for Comment, News-Feed (Posts) , Like on comments and posts

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True,null=True)
    picture = models.ImageField(upload_to='status_images',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(blank=True, default=0)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Like(models.Model):
    no_of_likes = models.IntegerField(default=0)
    sender = models.ForeignKey(User,related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver', blank=True, null=True)
    created_at = models.DateTimeField()
    picture = models.ImageField(upload_to='status_images',blank=True, null=True)
    status = models.ForeignKey(Post, blank=True, null=True)

    def __unicode__(self):
        return self.sender.username
