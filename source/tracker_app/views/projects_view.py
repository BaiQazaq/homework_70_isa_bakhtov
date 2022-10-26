from django.views.generic import ListView
from tracker_app.models import Project
from django.db.models import Q
from urllib.parse import urlencode

from tracker_app.forms import SearchForm


class ProjectIndexView(ListView):
    template_name = 'projects_list.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('-created_at',)
    queryset = Project.objects.exclude(is_deleted=True)
    paginate_by = 2
    allow_empty = True
    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)
    
    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
            if len(queryset) == 0:
                return queryset
        return queryset
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['text'] = {'text' : 'Project not found'}
            context['query'] = urlencode({'search': self.search_value})
        return context