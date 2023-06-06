from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(null=True)
    screen = models.ImageField(upload_to='photos/')
    secondscreen = models.ImageField(upload_to='photos/', null=True, blank=True)
    thirdscreen = models.ImageField(upload_to='photos/', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Question(models.Model):
    author = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'Author: {self.author}'


# Create your models here.
