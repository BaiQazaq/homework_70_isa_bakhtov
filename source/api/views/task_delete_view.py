from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers.task_serializer import TaskSerializer
from tracker_app.models import Task


class TaskDeleteView(APIView):
    
    def delete(self, request, *args, **kwargs):
        object = Task.objects.get(pk = kwargs['pk'])
        serializer = TaskSerializer(data=object.__dict__)
        if serializer.is_valid():
            object.delete()
            return Response(object.pk)
        else:
            return Response(serializer.errors, status=400)