#from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category, Page , UserProfile
from rango.forms import PageForm,CategoryForm, UserProfileForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
"""
def index(request):
    context = RequestContext(request)
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'pages': page_list}
    return render_to_response('rango/index.html', context_dict, context)
"""

def category_list(request):
    context = RequestContext(request)
    category_dict = Category.objects.order_by('-name')
    context_dict = {'categorys':category_dict}
    return render_to_response('rango/category_list.html', context_dict, context)


def home(request):
    context = RequestContext(request)
    user = request.user

    return render_to_response('rango/home.html',{},context)


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-name')
    context_dict = {'categorys': category_list}
    return render_to_response('rango/index.html', context_dict, context)



def about(request):
    context = RequestContext(request)
    hosts = request.get_host()
    context_dict = {'boldmessage': "Its a demo Social-Network Project",'host':hosts}
    return render_to_response('rango/index.html', context_dict, context)


def category(request, category_name_url):
    context = RequestContext(request)

    category_name = category_name_url.replace('_',' ')
    context_dict = {'category_name': category_name}
    context_dict['categoryname'] = category_name_url

    try:
        category = Category.objects.get(name=category_name)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category


    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)


def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #if form.is_valid():
        form.save(commit=True)
        return index(request)
        #else:
            #print form.errors
    else:
        form = CategoryForm()
    return render_to_response('rango/add_category.html', {'form':form}, context)


def add_page(request, category_name_url):
    context = RequestContext(request)

    #category_name = decode_url(category_name_url)

    category_name = category_name_url#.replace('_',' ')

    if request.method == 'POST':
        form = PageForm(request.POST)


        if form.is_valid():
            page = form.save()
            page.category = category_name
            """
            try:
                cat = Category.objects.get(name=category_name)
                print cat
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response('rango/add_category.html',{},context)
            """
            #page.views = 0
            page.save()

            return category(request, category_name_url)
        else:
            print form.errors
            #return category(request, category_name_url)

    else:
        form = PageForm()

    return render_to_response('rango/add_page.html',
        {'category_name_url': category_name_url,
         'category_name': category_name,'form':form},
        context)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'rango/register.html',
        {'user_form':user_form, 'profile_form':profile_form, 'registered': registered},
        context)

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)#find answers
        ankit = 'ankit'

        if user:
            if user.is_active:
                login(request, user)
                if request.user.is_authenticated():
                    return HttpResponseRedirect(reverse('profile', kwargs={}))
                    #return HttpResponseRedirect('/rango/profile/')
                #profile(request, username)
                #return profile(request)
                #return HttpResponseRedirect(reverse('profile', kwargs={'user_name':username}))
                #return HttpResponseRedirect(reverse('profile', kwargs={}))
            else:
                return HttpResponse("your django account is disabled.")
        else:
            print "Invalid login detailsw "
            return HttpResponse("invalid login details supplied")

    else:
        return render_to_response('rango/login_css.html', {}, context)

@login_required()
def profile(request):


    context = RequestContext(request)

    """
    #profile_name = profile_name_url
    #user_name = 'user_name'
    #emails = user_name.password
    #no_of_likes = 0
    #return HttpResponse(user_name1)
    """
    user_name = request.user.username


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
                    #'no_of_likes':12,
                    }

    if request.method == 'POST':
        #no_of_like = request.POST['no_of_likes']
        #no_of_likes = no_of_likes+1

        #sender = request.POST['sender']
        #receiver_profile = UserProfile.objects.get(user__username__exact=user_name)
        exists = False
        receiver=user_profile.user

        profile_dict = {'username':request.user.username,
                        'title': title,
                        'email': email,
                        'website': website,
                        'picture': picture,
                        }


        return render_to_response('rango/profile.html',profile_dict, context)
    else:
        print user_name
        #logout_view(request)
        #return HttpResponse(user_name.password)
        #render(request, 'rango/profile.html', profile_dict)
        return render_to_response('rango/profile.html', profile_dict, context)

    #logout(request)

def logout_view(request):
    logout(request)
    return home(request)


#use httpresponseredirect(reverse(ababab), kwargs=kagahsg)

def profile1(request, user_name1):


    context = RequestContext(request)

    #profile_name = profile_name_url
    #user_name = 'user_name'
    #emails = user_name.password
    #no_of_likes = 0
    #return HttpResponse(user_name1)
    user_name = request.user.username


    user_profile = UserProfile.objects.get(user__username__exact=user_name1)
    website= user_profile.website
    picture = user_profile.picture
    title = user_profile.title
    email = user_profile.user.email
    profile_dict = {'username':user_name1,
                    'title': title,
                    'email': email,
                    'website': website,
                    'picture': picture,
                    #'no_of_likes':12,
                    }
    return render_to_response('rango/profile.html',profile_dict, context)

