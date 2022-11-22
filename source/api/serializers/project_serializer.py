from rest_framework import serializers

from tracker_app.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'start_date', 'finish_date',  'title', 'description', 'created_at', 'changed_at')
        read_only_fields = ('id',  'created_at', 'changed_at')
        
    def create(self, validated_data):
        return Project.objects.create(**validated_data)


    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance