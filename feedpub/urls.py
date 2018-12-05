from django.conf.urls import include, url, path
from django.contrib import admin
from . import views

app_name = 'feedpub'


###ORIGINAL###
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('', include(admin.site.urls)),
#]

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(admin.site.urls)), ##from ORIGINAL above
    path('feed/<int:feed_id>/alexa/', views.alexafile, name='alexafile'),
    path('feed/<int:feed_id>/google/', views.googlefile, name='googlefile'),
    path('feed/<int:feed_id>/', views.feed, name='feed'),
    path('feeditem/<int:feeditem_id>/', views.feeditem, name='feeditem'),
    path('newitem/', views.newitem, name='newitem')
]
