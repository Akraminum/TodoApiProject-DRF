from django.test import TestCase

from Tasks.tests import print_task
from .models import ListModel

# Create your tests here.
print("\t### Lists ###")

def testino_on_object():
    # list object 
    list = ListModel.objects.all().first()

    # get related many objects
    # backward relation always hit database again and perform join in python [[FUCK]]
    list_tasks = list.tasks.all()
    print(f'list_tasks Total count: {list_tasks.count()}')

    list_tasks = list_tasks.filter(isDone=False)
    # list_tasks = list_tasks.filter(name__contains='C')
    
    [print_task(task) for task in list_tasks]

def testino_on_query():
    # lists_query = ListModel.objects.prefetch_related('tasks').first()

    # # for list in lists_query:
    # print(f"list: {lists_query.name}")
    # for task in lists_query.tasks.all():
    #     print(task.name)

    # ####### multiple
    # lists_query = ListModel.objects.prefetch_related('tasks').all()

    # for list in lists_query:
    #     print(f'{list.name} ({list.tasks.count()})')
    #     for task in list.tasks.all():
    #         print(task)
    from django.db import connection
    print(connection.queries)

    lists_query = ListModel.objects.prefetch_related('tasks__priority').all()

    for list in lists_query: #1
        print(f'{list.name} ({list.tasks.count()})') #4
        for task in list.tasks.all(): # 4
            print(f'{task.name} ({task.priority.name})')
 
    for q in connection.queries:
        print(f'{q}\n')
    print(len(connection.queries))
    




    



# testino_on_object()
testino_on_query()








print()