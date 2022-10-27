from django.contrib.auth.models import User
from django.db import models

from tracker_app.models import Project

class ProjectUser(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='users_project',
        verbose_name="User's project",
        null=False,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name ='projects_user',
        verbose_name = "User's project",
        null=False,
        on_delete=models.CASCADE
    )
    
    
    class Meta:
        verbose_name = 'Project of user'
        verbose_name_plural = 'Projects of user'