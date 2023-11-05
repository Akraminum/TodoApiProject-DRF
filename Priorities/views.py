from rest_framework import mixins, generics
from django.db import connection


from .models import PriorityModel
from .Serializers import PriorityModelSerializer
# Create your views here.


class PriorityModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = PriorityModel.objects.all()
    serializer_class = PriorityModelSerializer
    

class PriorityModelDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriorityModel.objects.all()
    serializer_class = PriorityModelSerializer
    lookup_field = 'id'