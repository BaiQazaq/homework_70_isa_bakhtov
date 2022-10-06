from django.db import models


class Status(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=20,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'