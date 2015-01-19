from django.conf.urls import url, patterns
from friends import views

urlpatterns = patterns('',
                       #url(r'^friends_list$',views.friends_list , name='friends_list'),
                       url(r'^add_friend/$', views.add_friend, name='add_friend'),
                       url(r'^my_friends/$', views.my_friends, name='my_friends'),
                       url(r'^my_requests/$', views.my_requests, name='my_requests'),
                       )
