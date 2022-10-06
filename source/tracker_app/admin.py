from django.contrib import admin

from tracker_app.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","summary", "description", "status", "type", "created_at")
    list_filter = ("id", "summary", "description", "status", "type", "created_at")
    search_fields = ("summary", "description", "status", "type")
    fields = ("summary", "description", "status", "type", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Task, TaskAdmin)