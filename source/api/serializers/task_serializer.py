from rest_framework import serializers

from tracker_app.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description',  'status', 'type', 'project', 'created_at', 'changed_at')
        read_only_fields = ('id',  'created_at', 'changed_at')