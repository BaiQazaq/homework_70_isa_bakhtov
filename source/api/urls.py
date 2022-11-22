from django.urls import path

from api.views.project_view import ProjectView
urlpatterns = [
    path("project/<int:pk>/", ProjectView.as_view(), name='project_detail'),
]