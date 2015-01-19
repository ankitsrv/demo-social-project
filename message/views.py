from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from message.models import Message
from message.forms import ComposeForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .serializers import MessageSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from newsfeed.models import Post
# Create your views here.

#class Inbox(View):

def home(request, user_name):
    context = RequestContext(request)
    if request.user.is_authenticated():
        user_name1 = request.user
        return  render_to_response('message/home.html',{'username':user_name1},context)
    else:
        return HttpResponse("User is not logged in")

def inbox(request, user_name):

    """
    Displays a list of received messages for the current user.
    Optional Arguments:
        ``template_name``: name of the template to use.
    """
    #objects = MessageManager()
    recipient = User.objects.get(username__exact= user_name)
    context_instance=RequestContext(request)

    #template_name = 'inbox.html'

    message_list = Message.objects.filter(recipient=recipient)

    return render_to_response('message/sent_box.html', {
        'message_list': message_list,'username':user_name
    },context_instance)




#class Sent_message(request):

def sent_box(request, user_name):

    """
    Displays a list of sent messages by the current user.
    Optional arguments:
        'template_name: name of the template to use.
    """

    #template_name= 'sent_box.html'
    sender = User.objects.get(username__exact= user_name)
    #return HttpResponse(user_name)

    message_list = Message.objects.filter(sender=sender)

    return render_to_response('message/sent_box.html', {
        'message_list': message_list, 'username':user_name
    }, context_instance=RequestContext(request))

#class Create_message(request, form_class=ComposeForm):



def compose(request, user_name):

    #form_class = ComposeForm

    if request.method == "POST":
        #form_class.sender = request.user

        subject = request.POST['subject']
        body = request.POST['body']
        sender = User.objects.get(username__exact=user_name)
        recipient1 = request.POST['recipient']
        recipient = User.objects.get(pk=recipient1)

        #sender = User.objects.get(pk=sender1)

        #sender = User.objects.get(use)
        #form_class = ComposeForm(data=request.POST)
        message = Message(body=body,sender=sender,subject=subject,recipient=recipient)
        message.save()

        #if message.is_valid():
            #sender = request.user
            #form_class.save()
        id = message.id
        #msg = Message.objects.filter(sender = sender)
        #return HttpResponseRedirect('/home/message/sent-message/')
            #sender = form_class.sender
        return HttpResponseRedirect(reverse('view_message',kwargs={'message_id':id}))
    else:
        form_class = ComposeForm()
        #return HttpResponse(request.user)
        return render_to_response('message/compose.html',
                              {'form': form_class, 'user_name':user_name },
                              context_instance=RequestContext(request))


def view_message(request, message_id):
    form_class = ComposeForm
    #template_name = 'view_message.html'
    #user = User.objects.get(username__exact=user_name)

    now = timezone.now()

    message = Message.objects.get(id=message_id)

    """
    if (message.sender != user) and (message.recipient != user):
        raise Http404
    """

    #message.save()
    #context = {'message': message}

    #if message.recipient == user:
    #if message.sender == user:
    form = {
         'body': message.body,
         'subject': message.subject,
         'recipient': message.recipient,
         'sender' : message.sender,
         'sent_at': message.sent_at,
         'username': request.user,

     }
    context = message
    context_instance = RequestContext(request)
    return render_to_response('message/view_message.html',form,context_instance)

# REST framework Demo (DRF)

#@api_view(['GET'])
class MessageView(generics.ListCreateAPIView):
    model = Post
    #serializer_class = MessageSerializer