from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'feedpub'


###ORIGINAL###
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('', include(admin.site.urls)),
#]

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url('', include(admin.site.urls)), ##from ORIGINAL above, REMOVED 12.5.18@8:30a
    url(r'^feed/(\d+)/alexa/$', views.alexafile, name='alexafile'),
    url(r'^feed/(\d+)/google/$', views.googlefile, name='googlefile'),
    url(r'^feed/(\d+)/$', views.feed, name='feed'),
    url(r'^feeditem/(\d+)/$', views.feeditem, name='feeditem'),
    url(r'^newitem/$', views.newitem, name='newitem')
]
