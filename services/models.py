from django.db import models

class Services(models.Model):
    servise_name = models.CharField(max_length=120)
    about_service = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.servise_name}"