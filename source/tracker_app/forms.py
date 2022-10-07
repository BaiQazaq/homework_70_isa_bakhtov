from django import forms
from django.core.exceptions import ValidationError

from tracker_app.models import Task
from tracker_app.models import Type
from tracker_app.models import Status


class TaskForm(forms.ModelForm):
    types = forms.ModelChoiceField(required=False, label='Типы', queryset=Type.objects.all())
    statuses = forms.ModelChoiceField(required=False, label='Статусы', queryset=Status.objects.all())
    
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type', 'statuses')
    
    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 2:
            raise ValidationError('Заголовок должен быть длинее 2x символов')
        return summary
    
    def __str__(self):
        return self.statuses
    
# class TypeForm(forms.ModelForm):
#     types = forms.ModelChoiceField(required=False, label='Типы', queryset=Type.objects.all())
    
    
#     class Meta:
#         model = Type
#         fields = ('types')
    
    
# class StatusForm(forms.ModelForm):
    
    
#     class Meta:
#         model = Status
        
