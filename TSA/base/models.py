from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.username