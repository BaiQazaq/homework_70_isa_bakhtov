from django.urls import path

from tracker_app.views.tasks_view import IndexView
from tracker_app.views.task_view import TaskView
#from tracker_app.views.tasks_methods import add_view, detail_view, update_view, delete_view, confirm_delete

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/<int:pk>", TaskView.as_view(), name='task_render')
    # path("tasks/add/", add_view, name='creation'),
    # path("task/<int:pk>/update/", update_view, name='update'),
    
    # path("task/<int:pk>/delete/", delete_view, name= "delete"),
    # path("task/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]