from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from tasks.models import Task
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project_detail = get_object_or_404(Project, id=id)
    context = {
        "project_detail": project_detail,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def project_list_update(request, id):
    project_list_object = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project_list_object)
        if form.is_valid():
            list = form.save()
            return redirect("show_project", id=list.id)
    else:
        form = ProjectForm(instance=project_list_object)
    context = {
        "project_list_object": project_list_object,
        "form": form,
    }
    return render(request, "projects/edit.html", context)


@login_required
def project_list_delete(request, id):
    model_instance = Project.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("list_projects")
    context = {
        "project_detail": get_object_or_404(Project, id=id)
    }
    return render(request, "projects/delete.html", context)


class ProjectTimelineView(LoginRequiredMixin, ListView):
    login_url = "accounts:login"
    template_name = "projects/project_timeline.html"
    model = Task
    context_object_name = "completed_tasks"

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Task.objects.filter(project_id=project_id).order_by("due_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs["project_id"]
        project = Project.objects.get(id=project_id)
        context["project"] = project
        context["task_count"] = Task.objects.filter(project_id=project_id).count()
        context["completed_count"] = Task.objects.filter(project_id=project_id, is_completed=True).count()
        return context
