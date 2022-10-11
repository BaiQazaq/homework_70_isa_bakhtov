from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator

from tracker_app.models import Task

def upper_validator(string):
    if not string[0].isupper():
        raise ValidationError('First letter must be in Uppercase')
    return string
    

class TaskForm(forms.ModelForm):
    summary = forms.CharField(label='Заголовок', max_length=100, required=True, validators=(MaxLengthValidator(limit_value=100), MinLengthValidator(limit_value=2), upper_validator))
        
    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
    
    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        # if len(summary) < 2:
        #     raise ValidationError('This value is too short!')
        if Task.objects.filter(summary=summary).exists():
            raise ValidationError ("Text of the article should not duplicate it's title!")
        return summary
    
    
   
    
