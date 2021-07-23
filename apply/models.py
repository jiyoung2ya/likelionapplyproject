from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Apply(models.Model):
    name = models.CharField(max_length=10)
    student_id = models.CharField(max_length=10)
    major = models.CharField(max_length=15)
    q1 = models.TextField(max_length=300)
    q2 = models.TextField(max_length=300)
    q3 = models.TextField(max_length=300)
    q4 = models.TextField(max_length=300)
    date = models.DateTimeField()