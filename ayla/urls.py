#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test_django 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/8/5 22:29 
'''
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^area/$', views.search_area),
]
