from datetime import datetime
from rest_framework import serializers

from Priorities.Serializers import PriorityModelSerializer

from .models import TaskModel


class TaskModelOutputSerializer(serializers.ModelSerializer):
    priority = PriorityModelSerializer()
    
    class Meta:
        model = TaskModel
        fields = [
            'id',
            'name',
            'description',
            'isDone',
            'dateCreated',
            'dateDue',
            'dateCompleted',
            'priority',
            'list_id',
        ]


class TaskModeInputSerializer(serializers.ModelSerializer):
    # list_id = serializers.IntegerField()
    # priority_id = serializers.IntegerField()
    
    class Meta:
        model = TaskModel
        fields = [
            'id',
            'name',
            'description',
            'dateDue',
            'priority',
            'list',
        ]

    # def validate_dateDue(self, value: datetime):
    #     print(type(value))
    #     if value.date() < datetime.today().date():
    #         raise serializers.ValidationError("Date due cannot be in the past")
    #     return value
    
    def validate(self, data:dict):
        if data.get('dateCreated', None) == None : # not exist
            # create case, assert that due >= today
            if data['dateDue'].date() < datetime.today().date():
                raise serializers.ValidationError("Date due cannot be in the past")
        else:
            # update case, asser that due >= creat
            if data['dateDue'].date() < data['dateCreated'].date():
                raise serializers.ValidationError("Date due cannot be in the past")
        return data
    
    


# print(repr(TaskModeInputSerializer())) 
 