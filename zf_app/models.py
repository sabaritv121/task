from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from zf_app.validator import validate_file_size


class Login(AbstractUser):

    is_adm = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class adm(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='admin')
    name = models.CharField(max_length=100)
    dob =models.DateField(max_length=100)
    contact_no = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to='profilepic/',validators=[validate_file_size])


    def __str__(self):
        return self.name


class student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=100)
    dob =models.DateField(max_length=100)
    contact_no = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to='profile/',validators=[validate_file_size])

    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days / 365.25)

    def __str__(self):
        return self.name


class marks(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE, related_name='student')
    mark = models.IntegerField()
    def __str__(self):
        return self.name
