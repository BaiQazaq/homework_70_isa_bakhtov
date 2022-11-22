from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from api.serializers.project_serializer import ProjectSerializer
from tracker_app.models import Project

class ProjectView(View):
    
    def get(self, request, *args, **kwargs):
        object = Project.objects.get(pk = kwargs['pk'])
        serializer = ProjectSerializer(object)
        return JsonResponse(serializer.data)
    

class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.filter(pk = kwargs['pk'])
        serializer = ProjectSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)
