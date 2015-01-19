import datetime
from django import forms
from message.models import  Message

class ComposeForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ['sender']

"""
    def save_message(self, sender):

        message = super(ComposeForm, self).save()

        # Save first and last name
        # user = message

        message.recipient = self.cleaned_data['recipient']
        message.subject = self.cleaned_data['subject']
        message.body = self.cleaned_data['body']

        message.save()

        return message

"""