from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    telegram_id = models.IntegerField()


