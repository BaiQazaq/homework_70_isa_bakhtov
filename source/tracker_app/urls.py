from django.urls import path

from tracker_app.views.tasks_view import IndexView
from tracker_app.views.task_view import TaskView
from tracker_app.views.task_edit_view import TaskEditView
from tracker_app.views.task_create_view import TaskCreateView
from tracker_app.views.task_delete import delete_view, confirm_delete


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/<int:pk>", TaskView.as_view(), name='task_render'),
    path("task/<int:pk>/update/", TaskEditView.as_view(), name='task_edit'),
    path("tasks/add/", TaskCreateView.as_view(), name='task_creation'), 
    path("task/<int:pk>/delete/", delete_view, name= "delete"),
    path("task/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]