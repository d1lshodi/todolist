from django.contrib import admin
from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username','email','id','is_active']

admin.site.register(UserModel, UserModelAdmin)
