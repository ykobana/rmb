from django.db import models

# Create your models here.


class Chat(models.Model):
    date = models.DateTimeField('date published')
    name = models.CharField(max_length=128)
    message = models.CharField(max_length=256)
