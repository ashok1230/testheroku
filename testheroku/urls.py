from django.conf.urls import patterns, include, url
from django.contrib import admin
from herokuapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testheroku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 		Home),
    url(r'^deep/$',		Deep),
)
