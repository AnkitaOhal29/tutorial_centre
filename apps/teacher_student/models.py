from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
UserType =(
    ("student", "Student"),
    ("teacher", "Teacher"),
)

class User(AbstractUser):
   user_type = models.CharField(max_length=10, choices= UserType)
   USERNAME_FIELD = 'username'


class Subject(models.Model):
    name      = models.CharField(max_length=100)

    class Meta:
       ordering = ['-id']


class Teacher(models.Model):
    name      = models.CharField(max_length=100)
    subjects  = models.ManyToManyField(Subject)
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
       ordering = ['-id']


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers      = models.ManyToManyField(Teacher)
    
    class Meta:
       ordering = ['-id']

class assignment(models.Model):
    assignment   = models.CharField(max_length=100)
    user         = models.ManyToManyField(Student)
    teacher      = models.ManyToManyField(Teacher)
    
    class Meta:
       ordering = ['-id']