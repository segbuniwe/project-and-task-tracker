from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, NoteForm
from tasks.models import Task, Note
from projects.models import Project

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
        form.fields["project"].queryset = Project.objects.filter(
            owner=request.user
        )
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def list_tasks(request):
    task_list = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": task_list,
    }
    return render(request, "tasks/list.html", context)


@login_required
def task_list_update(request, id):
    task_list_object = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_list_object)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task_list_object)
    context = {
        "task_list_object": task_list_object,
        "form": form,
    }
    return render(request, "tasks/edit.html", context)


@login_required
def task_list_delete(request, id):
    model_instance = Task.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_my_tasks")
    context = {
        "task_detail": get_object_or_404(Task, id=id)
    }
    return render(request, "tasks/delete.html", context)


@login_required
def show_task(request, id):
    task_detail = get_object_or_404(Task, id=id)
    context = {
        "task_detail": task_detail,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = NoteForm()
        form.fields["task"].queryset = Task.objects.filter(
            assignee=request.user
        )
    context = {
        "form": form,
    }
    return render(request, "tasks/create_note.html", context)


@login_required
def note_update(request, id):
    note_object = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note_object)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = NoteForm(instance=note_object)
    context = {
        "task_list_object": note_object,
        "form": form,
    }
    return render(request, "tasks/edit_note.html", context)


@login_required
def note_delete(request, id):
    model_instance = Note.objects.get(id=id)
    note_detail = get_object_or_404(Note, id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("show_my_tasks")
    context = {
        "note_detail": note_detail
    }
    return render(request, "tasks/delete_note.html", context)
