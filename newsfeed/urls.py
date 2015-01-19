from django.conf.urls import url, patterns
from newsfeed import views

urlpatterns = patterns('',
                       #url(r'^(?P<user_name>\w+)/$',views.main , name='news'),
                       url(r'^$',views.main, name='news'),
                       url(r'^add_post/$', views.add_post, name='add_post'),
                       url(r'^check/$',views.demo_check,name='demo_check'),
                       url(r'^post/(?P<post_id>[\d]+)/$', views.comments, name='comments'),
                       #url(r'^add_post/(?P<user_name>\w+)/$', views.add_post, name='add_post'),
                       )
