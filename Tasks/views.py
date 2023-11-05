from rest_framework import mixins, generics

from .models import TaskModel
from .Serializers import TaskModelOutputSerializer, TaskModeInputSerializer


class TaskModelDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    # serializer_class = TaskModelOutputSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TaskModelOutputSerializer
        return TaskModeInputSerializer

class TaskModelListAPIView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    # serializer_class = TaskModeInputSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TaskModelOutputSerializer
        return TaskModeInputSerializer