from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from api.serializers.task_serializer import TaskSerializer
from tracker_app.models import Task

class TaskSimpleView(View):
    
    def get(self, request, *args, **kwargs):
        object = Task.objects.get(pk = kwargs['pk'])
        serializer = TaskSerializer(object)
        return JsonResponse(serializer.data)
    

class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Task.objects.filter(pk = kwargs['pk'])
        serializer = TaskSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)
