"""nav URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from navapp import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^second_url/$', views.second_url, name="second_url"),
    url(r'^second_url2/$', views.second_url2, name="second_url2"),
    url(r'^second_url3/$', views.second_url3, name="second_url3"),
]
