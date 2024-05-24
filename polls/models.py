from django.db import models


class Lesson(models.Model):
    name = models.CharField('lesson name', max_length=50, unique=True)
    slug = models.SlugField('Url', unique=True)
    description = models.TextField('Short Description lesson')
    about = models.TextField('Every about lesson')
    photo = models.ImageField('Photo Lesson', upload_to='lessons')

    def __str__(self):
        return self.name


class Student(models.Model):
    last_name = models.CharField(max_length=35)
    first_name = models.CharField(max_length=35)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True)
    video = models.FileField(upload_to='videos', blank=True)

    def __str__(self):
        return self.last_name
