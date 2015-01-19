from django.shortcuts import render
from django.utils import timezone
# Create your views here.

def feed(request):
    pass
from rango.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from newsfeed.forms import PostForm
from newsfeed.models import Post
from django.shortcuts import get_object_or_404
from django.template import RequestContext

# To print the all statuses

def main(request):
    # Main listing
    context = RequestContext(request)

    user_name = request.user.username
    user_profile = UserProfile.objects.get(user__username__exact=user_name)
    user = User.objects.get(username=user_name)
    posts = Post.objects.all().order_by('-created')

    #if request.method == 'POST':

        #comment = request.POST['comment']

        #return render_to_response('newsfeed/list.html',{'posts':posts},context)
    #else:

        #posts = Post.objects.get(user=user)
        #paginator = Paginator(posts, 10)

    return render_to_response('newsfeed/list.html',{'posts':posts}, context)

# Just checking if the CSS template is working

def comments(request, post_id):
    context = RequestContext(request)

    post = Post.objects.get(pk=post_id)
    comment = request.POST['comment']
    post.comment = comment
    post.save()
    posts = Post.objects.all().order_by('-created')
    return render_to_response('newsfeed/list.html',{'posts':posts}, context)

def demo():
    """
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    """
    #return HttpResponse(user.get_username())
    #return render_to_response("list.html", dict(posts=posts, user=request.user))
    pass

def add_post(request):
    #single post with comments and a comment form.
    #post = Post.objects.get(pk=int(post_id))
    context = RequestContext(request)
    user_name = request.user.username
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)

        post = post_form.save()
        title = request.POST['title']
        body = request.POST['body']

        #user = user_name
        user = User.objects.get(username__exact=user_name)
        created=timezone.now()

        user_profile = UserProfile.objects.get(user__username__exact=user_name)
        #post = Post(title=title, body=body, created=created, user=user)
        if 'picture' in request.FILES:
                post.picture = request.FILES['picture']

        website= user_profile.website

        post.save()
        #post = PostForm(data=request.POST)

        #comments = Comment.objects.filter(post=post)
        #d.update(csrf(request))
        #post.save()
        #return HttpResponse(post)
        return render_to_response('newsfeed/post.html', {'post':post} ,context)
        #return HttpResponse("Post got saved")
    else:
        form = PostForm(initial={'user':request.user})
        return render_to_response('newsfeed/add_post.html',{'form':form},context)


"""

def likes(request):

    if not exists:

            user_clicked = Like(receiver=receiver)
            user_clicked.no_of_likes = user_clicked.no_of_likes + 1
            likes = user_clicked.no_of_likes
            sender = user_clicked.receiver
            #user_clicked.save()

        else:
            user_clicked = Like.objects.get(receiver=receiver)
            user_clicked.no_of_likes = user_clicked.no_of_likes + 1
            likes = user_clicked.no_of_likes
            sender = user_clicked.receiver
            #user_clicked.save()

            context = RequestContext(request)

    if request.method == 'POST':


        #sender = request.POST['sender']

        likes = Like(sender=request.user, receiver=user_name)
        likes.no_of_likes = likes.no_of_likes + 1
        no_of_likes = likes.no_of_likes
        user_profile = UserProfile.objects.get(user__username__exact=user_name)
        website= user_profile.website
        picture = user_profile.picture
        title = user_profile.title
        email = user_profile.user.email
        profile_dict = {'username':user_name,
                        'title': title,
                        'email': email,
                        'website': website,
                        'picture': picture,
                        'no_of_likes':no_of_likes,
                        'sender': request.user,
                        }


        return render_to_response('rango/profile.html',profile_dict, context)

    else:
        return HttpResponse("kdksldsadb")
"""

def demo_check(request):
    context = RequestContext(request)
    return render_to_response('newsfeed/home_css.html',{'username':request.user.username},context)