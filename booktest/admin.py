from django.contrib import admin
from booktest.models import *

# Register your models here.
#自定义管理页面，比如列表页要显示哪些值
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name']

class RoleInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name', 'gender', 'comment']

# 将自定义的模型类在该模块下进行注册 才可以在后台管理中看到，并进行增删改查操作
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(RoleInfo, RoleInfoAdmin)