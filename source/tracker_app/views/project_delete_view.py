from tracker_app.models import Project
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('projects_list')
