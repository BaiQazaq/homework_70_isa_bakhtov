from rest_framework import serializers

from tracker_app.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'start_date', 'finish_date',  'title', 'description', 'created_at', 'changed_at')
        read_only_fields = ('id',  'created_at', 'changed_at')