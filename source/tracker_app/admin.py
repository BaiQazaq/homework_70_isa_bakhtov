from django.contrib import admin

from tracker_app.models import Task
from tracker_app.models import Type
from tracker_app.models import Status

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","summary", "description", "status", "type", "created_at")
    list_filter = ("id", "summary", "description", "status", "type", "created_at")
    search_fields = ("summary", "description", "status", "type")
    fields = ("summary", "description", "status", "type", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Task, TaskAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id","name", "created_at", "update_at")
    list_filter = ("id","name", "created_at", "update_at")
    search_fields = ("id","name", "created_at", "update_at")
    fields = ("id","name", "created_at", "update_at")
    readonly_fields = ("id", "created_at", "update_at")

admin.site.register(Type, TypeAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ("id","name", "created_at", "update_at")
    list_filter = ("id","name", "created_at", "update_at")
    search_fields = ("id","name", "created_at", "update_at")
    fields = ("id","name", "created_at", "update_at")
    readonly_fields = ("id", "created_at", "update_at")

admin.site.register(Status, StatusAdmin)