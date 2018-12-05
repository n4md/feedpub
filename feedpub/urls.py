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
    url('', views.index, name='index'),
    url('', include(admin.site.urls)), ##from ORIGINAL above
    url('feed/<int:feed_id>/alexa/', views.alexafile, name='alexafile'),
    url('feed/<int:feed_id>/google/', views.googlefile, name='googlefile'),
    url('feed/<int:feed_id>/', views.feed, name='feed'),
    url('feeditem/<int:feeditem_id>/', views.feeditem, name='feeditem'),
    url('newitem/', views.newitem, name='newitem')
]
