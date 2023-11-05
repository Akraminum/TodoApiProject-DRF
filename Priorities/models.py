from django.db import models


# Create your models here.
class PriorityModel(models.Model):
    name = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=7, default="#aaaaaa")

    class Meta:
        ordering = ["name"]