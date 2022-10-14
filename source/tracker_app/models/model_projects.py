from turtle import title
from django.utils import timezone

from django.db import models

# Create your models here.


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала', auto_now=False, auto_now_add=False, null=False, blank=False)
    finish_date = models.DateField(verbose_name='Дата окончания',auto_now=False, auto_now_add=False, null=False, blank=False)
    title = models.CharField(verbose_name='Заголовок', max_length=100, null=False, blank=False)
    description = models.CharField(verbose_name='Описание',max_length=500, null=True)
    task = models.ForeignKey('tracker_app.Task', verbose_name='Задача', related_name='projects', on_delete=models.PROTECT)

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    def __str__(self):
        return f"{self.title} - {self.description} - {self.start_date} - {self.finish_data}"
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()