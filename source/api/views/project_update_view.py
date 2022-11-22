# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers.project_serializer import ProjectSerializer
from tracker_app.models import Project


class ProjectUpdateView(APIView):
    
    def put(self, request, *args, **kwargs):
        object = Project.objects.get(pk = kwargs['pk'])
        serializer = ProjectSerializer(data=object.__dict__)
        if serializer.is_valid():
            object = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)