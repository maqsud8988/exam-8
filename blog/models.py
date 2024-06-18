from django.db import models

class Blog(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    explanation = models.TextField()
    image = models.ImageField()
    data = models.DateField
