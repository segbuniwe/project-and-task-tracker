from django.contrib import admin
from tasks.models import Task, Note

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "content",
        "is_completed",
    )
