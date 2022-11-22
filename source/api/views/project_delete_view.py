from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers.project_serializer import ProjectSerializer
from tracker_app.models import Project


class ProjectDeleteView(APIView):
    
    def delete(self, request, *args, **kwargs):
        object = Project.objects.get(pk = kwargs['pk'])
        serializer = ProjectSerializer(data=object.__dict__)
        if serializer.is_valid():
            object.delete()
            return Response(object.pk)
        else:
            return Response(serializer.errors, status=400)