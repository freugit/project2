from django.db import models
class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    def __str__(self):
        return self.school_name

class Manager(models.Model):
    manage_id = models.IntegerField()
    manage_name = models.CharField(max_length=20)
    my_school = models.OneToOneField(School)
    def __str__(self):
        return self.manage_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    my_school = models.ForeignKey("School")

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField("Teacher")
    
# Create your models here.
