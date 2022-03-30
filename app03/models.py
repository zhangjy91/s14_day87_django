from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_type = models.IntegerField(choices=((1, '管理员'),(2, '普通员工'),(3, '访客')))

class UserToken(models.Model):
    token = models.CharField(max_length=64)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)