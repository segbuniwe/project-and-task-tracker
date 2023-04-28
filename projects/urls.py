from django.urls import path
from projects.views import (
    list_projects,
    show_project,
    create_project,
    project_list_update,
    project_list_delete,
    ProjectTimelineView,
)


urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("<int:id>/edit/", project_list_update, name="project_list_update"),
    path("<int:id>/delete/", project_list_delete, name="project_list_delete"),
    path("<int:project_id>/timeline/", ProjectTimelineView.as_view(), name="project_timeline"),
]
