#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test_django 
@File    ：utils.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/11 17:08 
'''
import hashlib

def hash_code(s,salt='some_salt'):
    h = hashlib.sha256()
    s.join(salt)
    h.update(s.encode())
    return h.hexdigest()