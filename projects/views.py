from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

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
