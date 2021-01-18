from django.db import models
from django.urls import reverse


class Factory(models.Model):
    name = models.CharField('Название', max_length=25)
    place = models.TextField('Расположение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фабрики'
        verbose_name_plural = 'Фабрики'


class Types(models.Model):
    title = models.CharField('Вид', max_length=20)
    task = models.TextField('Описание')
    factory = models.ManyToManyField(Factory, verbose_name='Шоколад', related_name='Types_Factory' )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("types_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Шоколад'
        verbose_name_plural = 'Виды'