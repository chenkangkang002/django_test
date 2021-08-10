from django.db import models

# Create your models here.

class User(models.Model):
    '''用户模型'''
    gender = (
        ('male','男'),
        ('female','女'),
    )
    u_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.u_name

    class Meta:
        ordering = ['-c_time']  #对返回结果按照c_time降序
        verbose_name = '用户' #给模型取一个易读的名字
        verbose_name_plural = '用户'  #模型的复数形式的名字，如果没有次属性，默认加s
