from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from tracker_app.forms import TaskForm
from tracker_app.models import Task


class TaskEditView(TemplateView):
    template_name = 'task_edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_render', pk=task.pk)
        return render(request, 'task_edit.html', context={'form': form})
        