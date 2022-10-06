from django import forms
from django.core.exceptions import ValidationError

from tracker_app.models import Task


class ArticleForm(forms.ModelForm):
    
    
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
    
    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Заголовок должен быть длинее 2x символов')
        return summary