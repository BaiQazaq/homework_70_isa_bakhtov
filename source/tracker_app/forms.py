from email.policy import default
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import User

from tracker_app.models import Task, Project, ProjectUser

def upper_validator(string):
    if not string[0].isupper():
        raise ValidationError('First letter must be in Uppercase')
    return string
    

class TaskForm(forms.ModelForm):
    summary = forms.CharField(label='Заголовок', max_length=100, required=True, validators=(MaxLengthValidator(limit_value=100), MinLengthValidator(limit_value=2), upper_validator))
        
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type', 'project')
    
    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        # if len(summary) < 2:
        #     raise ValidationError('This value is too short!')
        if Task.objects.filter(summary=summary).exists():
            raise ValidationError ("Text of the article should not duplicate it's title!")
        return summary
    
    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')
    

class ProjectForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', max_length=100, required=True, validators=(MaxLengthValidator(limit_value=100), MinLengthValidator(limit_value=2), upper_validator))
    start_date = forms.DateField()
    
    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'finish_date', 'users')
        

class ProjectUserForm(forms.Form):
    user = forms.ModelMultipleChoiceField(required=False, label='Users', queryset=User.objects.all())