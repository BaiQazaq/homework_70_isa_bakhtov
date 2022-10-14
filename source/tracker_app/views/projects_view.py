from django.views.generic import ListView
from tracker_app.models import Project


class ProjectIndexView(ListView):
    template_name = 'project_index.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('-created_at',)
    

    