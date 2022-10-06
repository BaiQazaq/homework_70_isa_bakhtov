from django.utils import timezone

from django.db import models

# Create your models here.


class Task(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание',max_length=500, null=True)
    status = models.ForeignKey('tracker_app.Status', verbose_name='Статус', related_name='tasks', on_delete=models.PROTECT)
    type = models.ManyToManyField(to='tracker_app.Type', verbose_name='Тип', related_name='tasks', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    
    def __str__(self):
        return f"{self.status} - {self.description}"
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()