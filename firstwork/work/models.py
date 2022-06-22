from statistics import mode
from django.db import models

# Create your models here.

class Student(models.Model):

    fname = models.CharField(max_length=100, null=True, blank= False)
    lname = models.CharField(max_length=100, null=True, blank= False)
    username = models.CharField(max_length=100, null=True, blank= False)
    dob = models.DateField()
    location = models.CharField(max_length=100, null=True, blank= False)

    def __str__(self):
        return f"{self.fname}: {self.lname}: {self.username}: {self.dob} to {self.location}"

