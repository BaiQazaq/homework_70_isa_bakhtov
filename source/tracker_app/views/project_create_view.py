from django.urls import reverse_lazy
from tracker_app.models import Project
from django.views.generic import CreateView
from tracker_app.forms import ProjectForm

    

class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Project
    #success_url = 
    
    def get_success_url(self):
        return reverse_lazy('project_render', kwargs={'pk': self.object.pk})