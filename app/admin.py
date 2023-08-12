from django.contrib import admin
from .models import TaskModel

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_description', 'is_complete')