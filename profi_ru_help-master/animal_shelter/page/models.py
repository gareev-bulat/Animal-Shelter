from django.db import models


class NewsItem(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    date = models.DateField(verbose_name='Дата записи')

    def __str__(self):
        return self.title

class Animal(models.Model):
    photo = models.ImageField(upload_to='animal_photos')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name