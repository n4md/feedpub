from django.conf.urls import include, url, path
from django.contrib import admin
from . import views

app_name = 'feedpub'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(admin.site.urls)),
]

