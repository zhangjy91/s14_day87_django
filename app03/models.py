from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=5, decimal_places=2)