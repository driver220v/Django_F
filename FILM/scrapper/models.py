from django.db import models

# Create your models here.
from django.db import models


class Film(models.Model):
    # id = models.IntegerField(primary_key=True, serialize=True, verbose_name='ID')
    title = models.CharField(max_length=50, null=False, verbose_name='Title', primary_key=True)
    genre = models.CharField(max_length=40, verbose_name='Genre')
    premier = models.DateField(verbose_name='Premier date')
    avg_tomatometer = models.CharField(max_length=3, verbose_name='Tomato_Score')
    avg_audience_score = models.CharField(max_length=3, verbose_name='Audience Score')

    def __str__(self):
        return f'{self.title} tomatometer: {self.avg_tomatometer}, audience: {self.avg_audience_score}'

    # ф-ция для inserta в БД
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
