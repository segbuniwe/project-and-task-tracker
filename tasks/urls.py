from django.urls import path
from tasks.views import (
    create_task,
    list_tasks,
    task_list_update,
    task_list_delete,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("<int:id>/edit/", task_list_update, name="task_list_update"),
    path("<int:id>/delete/", task_list_delete, name="task_list_delete"),
]
