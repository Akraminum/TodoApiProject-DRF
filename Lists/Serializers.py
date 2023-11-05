from rest_framework import serializers

from Tasks.Serializers import TaskModelOutputSerializer
from Tasks.models import TaskModel

from .models import ListModel


class ListModelOutputSerializer(serializers.ModelSerializer):
    completed_tasks_count = serializers.SerializerMethodField(read_only=True)
    completed_tasks = TaskModelOutputSerializer(many=True,source='tasks_completed', read_only=True)
    incompleted_tasks = TaskModelOutputSerializer(many=True,source='tasks_incompleted', read_only=True)
    incompleted_tasks_count = serializers.SerializerMethodField()
    class Meta:
        model = ListModel
        fields = [
            'id',
            'name',
            'completed_tasks_count',
            'completed_tasks',
            'incompleted_tasks_count',
            'incompleted_tasks',
        ]

    def get_completed_tasks_count(self, obj):
        return obj.tasks_completed.__len__()

    def get_incompleted_tasks_count(self, obj):
        return obj.tasks_incompleted.__len__()



class ListModelInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = [
            'id',
            'name',
        ]
        


# from django.db import connection

# def testino():
#     print("\t### Lists ###")
#     # lists_query = ListModel.objects.prefetch_related('tasks__priority').all()
#     # condition on to-many
#     from django.db.models import Prefetch
#     lists_query = ListModel.objects\
#                         .prefetch_related(
#                             Prefetch('tasks', 
#                                 queryset=TaskModel.objects.select_related(
#                                     'priority'
#                                     ).filter(isDone=True),
#                                 to_attr='tasks_completed'
#                             ),
#                             Prefetch('tasks', 
#                                 queryset=TaskModel.objects.select_related(
#                                     'priority'
#                                     ).filter(isDone=False),
#                                 to_attr='tasks_incompleted'
#                             )
#                         ).all()

#     serializer = ListModelSerializer(lists_query, many=True) 
#     # print(repr(serializer))
#     # print(lists_query[0].tasks_completed.__len__())
#     print(f'{serializer.data[0]}')

#     # for list in lists_query:
#     #     print(f'{list.name} ({list.tasks.count()})')
#     #     for task in list.tasks.all():
#     #         print(task)

#     # print()
#     print(f"\t### Done {len(connection.queries)} ###")
    
#     # for q in connection.queries:
#     #     print(f'{q}\n')
#     print()



# testino()