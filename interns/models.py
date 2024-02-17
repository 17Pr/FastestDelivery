from django.db import models

# Create your models here.
class transporter(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    destination=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    gender=models.CharField(max_length=15)
class distrubuter(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    placeofpickup=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    mode=models.CharField(max_length=15)
    typeofproduct=models.CharField(max_length=15)
