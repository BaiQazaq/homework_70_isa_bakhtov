from django.shortcuts import get_object_or_404, redirect
from tracker_app.models import ProjectUser
from django.urls import reverse
from django.views.generic import  TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tracker_app.forms import Project, ProjectForm


class DeleteUserFromProject(LoginRequiredMixin, TemplateView):
    template_name = 'user_delete_from_project.html'
    form_class = ProjectForm
    model = Project
    pk_url_kwarg = 'pk'
    context_object_name = 'project'
    
    def get_success_url(self):
        return reverse('project_render', kwargs={'pk': self.object.pk})
    
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context = self.get_context_data(**kwargs)
        project_users = project.projects_user.all()
        context ['users'] = project_users
        context ['project'] = project
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        user = request.POST['user']
        if ProjectUser.objects.filter(user=user, project=project).exists():
            ProjectUser.objects.filter(user=user, project=project).delete()
        return redirect('projects_list')
    
