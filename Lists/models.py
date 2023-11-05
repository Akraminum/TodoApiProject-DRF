from django.db import models

# Create your models here.
class ListModel(models.Model):
    name = models.CharField(max_length=100, blank=False)

    @property
    def tasks_count(self):  
        return self.tasks.count()