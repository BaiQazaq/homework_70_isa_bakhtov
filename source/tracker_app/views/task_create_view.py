from django.shortcuts import render, redirect, get_object_or_404
from tracker_app.models import Task, Status, Type
from django.views.generic import TemplateView, FormView
from tracker_app.forms import TaskForm
from django.urls import reverse


# class TaskCreateView(FormView):
#     template_name = 'task_create.html'
#     extra_context = {
#         'statuses': Status.objects.all(),
#         'types' : Type.objects.all()
#         }



#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         #kwargs['instance'] = self.task
#         return kwargs


#     def form_valid(self, form):
#         self.task = form.save()
#         return super().form_valid(form)


#     def get_success_url(self):
#         return reverse('task_render', kwargs={'pk': self.task.pk})



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
        return render(request, 'task_creation.html', context={'form': form})