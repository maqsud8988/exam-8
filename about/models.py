from django.db import models

class OurTeam(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    country = models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}"