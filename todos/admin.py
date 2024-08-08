from django.contrib import admin
from .models import TodoModel


class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'created_at','is_done']

admin.site.register(TodoModel, TodoModelAdmin)
