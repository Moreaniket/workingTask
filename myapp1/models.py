from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    number=models.IntegerField()
    password=models.CharField(max_length=50)


class shubham(models.Model):
    name=models.CharField(max_length=50)
    photo=models.FileField(upload_to="images")


class customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    number=models.IntegerField()