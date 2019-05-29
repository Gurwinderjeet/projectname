from django.db import models

# Create your models here.
#to create tables in database

class UserRole(models.Model):
    role_id=models.AutoField(
        primary_key=True)
    role_name=models.CharField(
        max_length=225,
        default="",
        unique=True)
class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(
        max_length=225,
        default="",
        unique=True)
#run these commands to create table
#python manage.py makemigrations appname
#python manage.py migrate
