from django.contrib import admin
from .models import Tag, Task

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_datetime', 'deadline_datetime', 'is_done']
    list_filter = ['is_done', 'tags', 'created_datetime']
    filter_horizontal = ['tags']
    search_fields = ['content']