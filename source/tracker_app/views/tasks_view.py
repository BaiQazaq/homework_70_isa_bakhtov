from django.views.generic import ListView
from tracker_app.models import Task


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('-created_at',)
    paginate_by = 10