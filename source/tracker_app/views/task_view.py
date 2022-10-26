from django.shortcuts import get_object_or_404
from tracker_app.models import Task
from django.views.generic import TemplateView


class TaskView(TemplateView):
    template_name = 'task_render.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context