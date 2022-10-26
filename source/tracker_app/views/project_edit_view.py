from django.views.generic import  UpdateView

from tracker_app.forms import ProjectForm
from tracker_app.models import Project
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectEditView(LoginRequiredMixin, UpdateView):
    template_name = 'project_edit.html'
    form_class = ProjectForm
    model = Project
    pk_url_kwarg = 'pk'
    context_object_name = 'project'
    
    def get_success_url(self):
        return reverse('project_render', kwargs={'pk': self.object.pk})