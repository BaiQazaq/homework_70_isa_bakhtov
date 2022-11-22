from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers.task_serializer import TaskSerializer
from tracker_app.models import Task


class TaskUpdateView(APIView):
    
    def put(self, request, *args, **kwargs):
        object = Task.objects.get(pk = kwargs['pk'])
        serializer = TaskSerializer(data=object.__dict__)
        if serializer.is_valid():
            object = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)