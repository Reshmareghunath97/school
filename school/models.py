from django.db import models
from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     branch = models.CharField(max_length=10)

class Teacher(models.Model):
    Education = models.CharField(max_length=255)
    Experience = models.CharField(max_length=255)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    Assignedclass = models.CharField(max_length=255)
    Bloodgroup = models.CharField(max_length=255)
    Gender = models.CharField(max_length=255)
    Emailaddress = models.CharField(max_length=255)
    Phonenumber = models.CharField(max_length=255)


    def __str__(self):
        return self.Education


