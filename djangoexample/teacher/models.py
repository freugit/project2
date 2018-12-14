from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
