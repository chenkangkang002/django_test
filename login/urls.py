#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test_django 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/10 22:24 
'''
import captcha
from django.conf.urls import url
from django.urls import include, path

from login import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout),
]