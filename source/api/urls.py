from django.urls import path

from api.views.project_view import ProjectSimpleView, ProjectView
from api.views.task_view import TaskSimpleView
from api.views.project_update_view import ProjectUpdateView
from api.views.project_delete_view import ProjectDeleteView

urlpatterns = [
    path("project/<int:pk>/", ProjectView.as_view(), name='project_detail'),
    path("task/<int:pk>/", TaskSimpleView.as_view(), name='task_detail'),
    
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name='project_update'),
    path("task/<int:pk>/update/", ProjectUpdateView.as_view(), name='task_update'),
    
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name='project_delete'),
    path("task/<int:pk>/delete/", ProjectDeleteView.as_view(), name='task_delete'),
]