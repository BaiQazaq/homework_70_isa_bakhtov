# from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import  UpdateView#, TemplateView, FormView,
from tracker_app.forms import TaskForm
from tracker_app.models import Task
from django.urls import reverse


class TaskEditView(UpdateView):
    template_name = 'task_edit.html'
    form_class = TaskForm
    model = Task
    pk_url_kwarg = 'pk'
    context_object_name = 'task'
    
    def get_success_url(self):
        return reverse('task_render', kwargs={'pk': self.object.pk})

# class TaskEditView(FormView):
#     template_name = 'task_edit.html'
#     form_class = TaskForm


#     def dispatch(self, request, *args, **kwargs):
#         self.task = self.get_object()
#         return super().dispatch(request, *args, **kwargs)


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = self.task
#         return context


#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.task
#         return kwargs


#     def form_valid(self, form):
#         self.task = form.save()
#         return super().form_valid(form)


#     def get_success_url(self):
#         return reverse('task_render', kwargs={'pk': self.task.pk})


#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Task, pk=pk)

# # class TaskEditView(TemplateView):
# #     template_name = 'task_edit.html'
    
# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
# #         return context
    
# #     def get(self, request, *args, **kwargs):
# #         context = self.get_context_data(**kwargs)
# #         form = TaskForm(instance=context['task'])
# #         context['form'] = form
# #         return self.render_to_response(context)
    
# #     def post(self, request, *args, **kwargs):
# #         task = get_object_or_404(Task, pk=kwargs['pk'])
# #         form = TaskForm(request.POST, instance=task)
# #         if form.is_valid():
# #             task = form.save()
# #             return redirect('task_render', pk=task.pk)
# #         return render(request, 'task_edit.html', context={'form': form})
        