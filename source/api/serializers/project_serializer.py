from rest_framework import serializers

from tracker_app.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # start_date = serializers.DateTimeField(read_only=True)
    # finish_date = serializers.DateTimeField(read_only=True)
    # title = serializers.CharField(max_length=100, required=True)
    # description = serializers.CharField(max_length=500, allow_blank=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # changed_at = serializers.DateTimeField(read_only=True)
    
    
    
    
    class Meta:
        model = Project
        fields = ('id', 'start_date', 'finish_date',  'title', 'description', 'created_at', 'changed_at')
        read_only_fields = ('id',  'created_at', 'changed_at')