from django.test import TestCase

# Create your tests here.
from .models import TaskModel

def print_task(task):
    print(f'''[{task.id} - {task.name}]  
list:({task.list.id} - {task.list.name})
priority:({task.priority.id} - {task.priority.name})''')
    
print("\t### Tasks ###")


def testino():

    # get task with related models
    task = TaskModel.objects\
                .select_related('priority')\
                .first()
    # priority joined in the query
    # list queried again
    print_task(task)
# testino()















print()