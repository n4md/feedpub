"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include ##ADDED path 12.5.18@5:18a
from django.contrib import admin
from feedpub import views

urlpatterns = [
    url(r'^feedpub/', include('feedpub.urls')), ##ADDED 12.5.18@5:18a ##ADDED regex r'^feedpub/', 12.5.18@9:52a
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', admin.site.urls),
]
