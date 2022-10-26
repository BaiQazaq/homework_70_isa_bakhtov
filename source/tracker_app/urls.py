from django.urls import path

from tracker_app.views.tasks_view import IndexView
from tracker_app.views.task_view import TaskView
from tracker_app.views.task_edit_view import TaskEditView
from tracker_app.views.task_create_view import TaskCreateView
from tracker_app.views.task_delete import TaskDeleteView

from tracker_app.views.projects_view import ProjectIndexView
from tracker_app.views.project_create_view import ProjectCreateView
from tracker_app.views.project_view import ProjectView
from tracker_app.views.project_edit_view import ProjectEditView
from tracker_app.views.project_delete_view import ProjectDeleteView




urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/<int:pk>", TaskView.as_view(), name='task_render'),
    path("task/<int:pk>/update/", TaskEditView.as_view(), name='task_edit'),
    path("tasks/add/", TaskCreateView.as_view(), name='task_creation'), 
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name= "delete"),
    path("task/<int:pk>/confirm_delete/", TaskDeleteView.as_view(), name= "confirm_delete"),
    
    path("projects/", ProjectIndexView.as_view(), name = 'projects_list'),
    path("project/add/", ProjectCreateView.as_view(), name='project_creation'),
    path("project/<int:pk>", ProjectView.as_view(), name='project_render'),
    path("project/<int:pk>/update/", ProjectEditView.as_view(), name='project_edit'),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name= "project_delete"),
    path("project/<int:pk>/confirm_delete/", ProjectDeleteView.as_view(), name= "project_confirm_delete")
]