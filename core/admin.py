from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "status", "deadline", "created_at")
    list_filter = ("status", "deadline")
    search_fields = ("title", "client_email")

admin.site.register(Task, TaskAdmin)    
