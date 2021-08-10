#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：test_django 
@File    ：forms.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/11 0:20 
'''
from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):

    username = forms.CharField(label='用户名', max_length=128,
                               widget=forms.TextInput(
                                   attrs={'class':'form-control','placeholder':'Username','autofocus':''}
                               ))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class':'form-control','placeholder':'Password'}
                               ))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    username = forms.CharField(label='用户名', max_length=128,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': ''}
                               ))
    password1 = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password'}
                               ))
    password2 = forms.CharField(label='确认密码', max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password'}
                               ))
    email = forms.EmailField(label='邮箱',widget=forms.EmailInput(
                                    attrs={'class': 'form-control'}
                                ))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码',
                            required=True,
                            error_messages={
                            'required': '验证码不能为空'
                        })
