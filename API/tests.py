from django.test import TestCase
from Lists.Serializers import ListModelOutputSerializer

# Create your tests here.
print("\t### Console TEST ###\n")

from Lists.models import ListModel
from Priorities.models import PriorityModel
from Tasks.models import TaskModel

if ListModel.objects.all().count() == 0:
    ListModel.objects.create(name="List 1")
    ListModel.objects.create(name="List 2")
    ListModel.objects.create(name="List 3")
# print(ListModel.objects.all())

# get all lists 
list = ListModel.objects.first()

# include taskmodels
list_tasks = list.taskmodel_set.all()

print(list_tasks)

list_serializer = ListModelOutputSerializer(list, many=True)
print(list_serializer.data)




if PriorityModel.objects.all().count() == 0:
    priorities =  PriorityModel.objects.bulk_create([
                                    PriorityModel(name='P1'),
                                    PriorityModel(name='P2'),
                                    PriorityModel(name='P3'),
                                ]) 
# print(PriorityModel.objects.all())

 
if TaskModel.objects.all().count() == 0:
    TaskModel(name='Task A', priority_id=1, list_id=1).save()
    TaskModel(name='Task B', priority_id=2, list_id=1).save()
    TaskModel(name='Task C', priority_id=1, list_id=1).save() 
# print(TaskModel.objects.all())

task = TaskModel.objects.all().select_related('list')
# print(task.query)





print()
print()