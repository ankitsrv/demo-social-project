from django.shortcuts import render
from rango.models import UserProfile
from friends.models import *
from friends.forms import FriendShipForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
# Create your views here.

def add_friend(request):
    """
    used for displaying and managing friends
    """

    form = FriendShipForm()
    context = RequestContext(request)
    if request.method == 'POST':
        form = FriendShipForm(request.POST)
        user_id = request.POST['friend']
        user = get_object_or_404(User, id=user_id)
        #user = User.objects.get(id=user_id)

        #if form.is_valid():
        num_results = FriendShip.objects.filter(from_user=request.user, friend=user).exists()

        if num_results > 0:
            return HttpResponse("friendship already exists")

        #user = User.objects.get(id=80)
        else:
            user_id = request.POST['friend']
            user = User.objects.get(id=user_id)
            friend_manage = FriendShip(from_user=request.user, friend=user)
            friend_manage.save()
            return HttpResponse(" Friend Request Send Success-fully")

        #return my_friends(request)
        #return HttpResponseRedirect('/home/friends/my_friends/')
        #else:
            #return HttpResponse(" No friends in lsit")
    else:
        return render_to_response('friends/add_friend.html',{'form':form, 'user': request.user} ,context)


    #user = request.user
    #profile = UserProfile.objects.get(user=user)
    #full_name = user.get_full_name()
    #email = user.email
    #area_interest = profile.area_of_interest
    #designation = profile.designation
    #friends = FriendShip.objects.filter(user=request.user)

def my_friends(request):

    context = RequestContext(request)
    user = request.user
    friends = FriendShip.objects.filter(from_user=user)
    friends_list = []
    for friend in friends:
        friends_list.append(friend.friend)

    return render_to_response('friends/friend_list.html',{'friends':friends} , context )
    #return HttpResponse(friends_list)

# for displaying the friend requests





def my_requests(request):
    context = RequestContext(request)
    user = request.user

    friend_requests = FriendShipInvitation.objects.filter(friend=user)

    return render_to_response('friends/friend_requests.html', {'friend_requests':friend_requests}, context)

