from django.shortcuts import render, redirect
from tracker_app.models import Task
from django.views.generic import TemplateView
from tracker_app.forms import TaskForm


class TaskCreateView(TemplateView):
    template_name = 'task_create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        task_data = {
        'summary': request.POST.get('summary'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'type': request.POST.get('type')
        }
        task = Task.objects.create(**task_data)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_render', pk=task.pk)
        return render(request, 'task_creation.html', context={'form': form})