
from tracker_app.models import Task
from django.urls import reverse_lazy
from django.views.generic import DetailView

class TaskDeleteView(DetailView):
    template_name = 'task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')

# def delete_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     #task.delete()
#     return render(request, 'task_confirm_delete.html', context={'task': task})


# def confirm_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect('base')