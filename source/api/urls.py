from django.urls import path

from api.views.project_view import ProjectSimpleView, ProjectView
from api.views.task_view import TaskSimpleView

urlpatterns = [
    path("project/<int:pk>/", ProjectView.as_view(), name='project_detail'),
    path("task/<int:pk>/", TaskSimpleView.as_view(), name='task_detail'),
]