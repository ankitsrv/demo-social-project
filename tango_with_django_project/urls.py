from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rango/', include('rango.urls')),
    url(r'^home/newsfeed/', include('newsfeed.urls')),
    url(r'^home/message/', include('message.urls')),
    url(r'^home/friends/', include('friends.urls')),
    url(r'^demo/$',login_required(TemplateView.as_view(template_name="rango/home.html"))),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

# for Static Media Server
"""
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )
"""