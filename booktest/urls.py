#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test_django 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/7 22:05 
'''
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^area/$', views.search_area),
]
# 方式1：位置参数
# 直接使用小括号，通过位置参数传递给视图。
# url(r'^delete(\d+)/$',views.show_arg),
# def show_arg(request, id):
#     return HttpResponse('show arg %s' % id)

# 方式2：关键字参数
# 其中?P部分表示为这个参数定义的名称为id，可以是其它名称，起名做到见名知意。
# url(r'^delete(?P<id1>\d+)/$', views.show_arg),
# def show_arg(request, id1):
#     return HttpResponse('show arg %s' % id1)




