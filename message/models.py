from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts')
    contact = models.ForeignKey(User,related_name='other contacts')
    is_blocked = models.BooleanField(default=False)


class Message(models.Model):

    #The content of a message
    subject = models.CharField(max_length=80)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name="senter")
    recipient = models.ForeignKey(User, related_name="recipient")
    sent_at = models.DateTimeField(null=True, blank=True, default=timezone.now())
    #read_at = models.DateTimeField(blank=True, null=True)

    #objects = MessageManager()

    class Meta:
        verbose_name = 'message content'

    class Admin:
        pass

    def __unicode__(self):
        return self.subject

    def inbox_for(self, user):
        return self.filter(
            recipient=user,
        )

    def outbox_for(self, user):
        return self.filter(
            sender = user,
        )



"""
class MessageManager(models.Manager):

    def inbox_for(self, user):
        return self.filter(
            recipient=user,
        )

    def outbox_for(self, user):
        return self.filter(
            sender = user,
        )

"""