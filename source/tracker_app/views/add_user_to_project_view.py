from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from tracker_app.models import ProjectUser, Project
from tracker_app.forms import ProjectUserForm

class AddUserView(LoginRequiredMixin, FormView):
    form_class = ProjectUserForm
    
    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            if not ProjectUser.objects.filter(user=user[0], project=project).exists():
                projectuser = ProjectUser(user=user[0], project=project)
                projectuser.save()
        return redirect('projects_list')
    