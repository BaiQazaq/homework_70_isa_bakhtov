from django.views.generic import DetailView
from tracker_app.models import Project


class ProjectView(DetailView):
    template_name = 'project_render.html'
    model =  Project
    pk_url_kwarg = 'pk'