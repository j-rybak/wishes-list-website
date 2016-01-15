# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'activate/(?P<code>[A-Za-z0-9\d]+)/', views.activate, name='activate'),
        url(r'login/$', views.login, name='login'),
        url(r'register/$', views.register, name='register'),
]
