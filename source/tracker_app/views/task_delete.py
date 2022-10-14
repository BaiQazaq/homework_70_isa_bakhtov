from django.shortcuts import render, redirect, get_object_or_404
from tracker_app.models import Task


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    #task.delete()
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('base')