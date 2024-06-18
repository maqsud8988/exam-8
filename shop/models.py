from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    price = models.IntegerField()