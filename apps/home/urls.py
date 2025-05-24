# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    path('', views.servers, name='servers'),
    path('create', views.create, name='create'),
    path('start', views.start, name='start'),
    path('stop', views.stop, name='stop'),
    path('edit', views.edit, name='edit'),
    path('reset', views.reset, name='reset'),
    path('delete', views.delete, name='delete'),
    path('exec', views.exec, name='exec'),
    path('user', views.user, name='user'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
