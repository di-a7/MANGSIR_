from django.contrib import admin
from .models import Todolist

# Register your models here.
# admin.site.register(Todolist)

# @admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ('id','title','description','status')
   list_filter = ['status']
   list_editable = ['status']
   list_per_page = 5
   search_fields = ['title','id']

admin.site.register(Todolist, TodolistAdmin)
