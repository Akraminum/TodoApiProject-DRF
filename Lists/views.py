from rest_framework import mixins, generics
from rest_framework.response import Response
from django.db.models import Prefetch

from Tasks.models import TaskModel

from .models import ListModel
from .Serializers import ListModelOutputSerializer, ListModelInputSerializer
# Create your views here.

list_retrieve_query_set = ListModel.objects\
                        .prefetch_related(
                            Prefetch('tasks', 
                                queryset=TaskModel.objects.select_related(
                                    'priority'
                                    ).filter(isDone=True),
                                to_attr='tasks_completed'
                            ),
                            Prefetch('tasks', 
                                queryset=TaskModel.objects.select_related(
                                    'priority'
                                    ).filter(isDone=False),
                                to_attr='tasks_incompleted'
                            )
                        ).all()


# ListCreateAPIView
class ListModelListCreateView(generics.ListCreateAPIView):
    
    def get_queryset(self):
        if self.request.method == 'POST':
            return ListModel.objects.all()
        return list_retrieve_query_set
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ListModelInputSerializer
        return ListModelOutputSerializer
    


class ListModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            return list_retrieve_query_set
        return ListModel.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListModelOutputSerializer
        return ListModelInputSerializer

    