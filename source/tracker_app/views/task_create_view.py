from django.shortcuts import render, redirect
from tracker_app.models import Task, Status, Type
from django.views.generic import TemplateView
from tracker_app.forms import TaskForm



class TaskCreateView(TemplateView):
    template_name = 'task_create.html'
    extra_context = {
        'statuses': Status.objects.all(),
        'types' : Type.objects.all()
        }
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return self.render_to_response(context={'form': form})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            type = form.cleaned_data.pop('type')
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
            )
            task.type.set(type)
            return redirect('task_render', pk=task.pk)
        return render(request, 'task_create.html', context={'form': form})