from django.db import models
from datetime import datetime

from Priorities.models import PriorityModel
from Lists.models import ListModel

# Create your models here.
class TaskModel(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    isDone      = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now=True) # gte today 
    dateDue     = models.DateTimeField(null=True) # gte today date
    dateCompleted = models.DateTimeField(null=True)

    priority    = models.ForeignKey(
                        PriorityModel, 
                        on_delete=models.SET_NULL, 
                        related_name='priorities', 
                        null=True
                        )
    list        = models.ForeignKey(
                            ListModel, 
                            on_delete=models.CASCADE,
                            related_name='tasks'
                            )
    # TODO
    # + UserCreatedId
    # + UserCompletedId


    

