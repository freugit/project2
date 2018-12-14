from django.db import models
class Person(models.Model):
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.name
# Create your models here.
