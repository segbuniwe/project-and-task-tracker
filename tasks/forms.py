from django.forms import ModelForm
from tasks.models import Task, Note


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "is_completed",
            "project",
            "assignee",
        )


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = (
            "content",
            "task",
            "is_completed",
        )
