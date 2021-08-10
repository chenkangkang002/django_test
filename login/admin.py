from django.contrib import admin

# Register your models here.
from login.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['u_name','email','sex','c_time']

admin.site.register(User, UserAdmin)
