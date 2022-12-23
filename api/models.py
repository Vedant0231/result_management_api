from django.db import models

# Create your models here.
"""student table model"""
class Student(models.Model):

    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    std = models.IntegerField()
    result = models.CharField(max_length=20)
    checkby = models.CharField(max_length=20)