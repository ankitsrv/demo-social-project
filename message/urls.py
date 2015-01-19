from django.conf.urls import url, patterns
from message.views import *
from message import views

urlpatterns = patterns('',
                       url(r'^message/(?P<user_name>\w+)/$', views.home, name='message'),

                       url(r'^inbox/(?P<user_name>\w+)/$', views.inbox, name='inbox'),

                       url(r'^sent_messages/(?P<user_name>\w+)/$',views.sent_box, name='sent_message'),

                       url(r'^compose/(?P<user_name>\w+)/$',views.compose, name='create_new_message'),
                       #url(r'^inbox/(?P<message_id>\d)$', views.view_message, name='view_inbox_message'),

                       url(r'^sent_message/(?P<message_id>[\d]+)/$', views.view_message, name='view_message'),

                       url(r'views/$', views.MessageView.as_view(), name='message view'),

                       )




