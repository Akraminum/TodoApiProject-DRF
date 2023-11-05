from django.urls import path
from .views import ListModelDetailView, ListModelListCreateView

urlpatterns = [
    path('', ListModelListCreateView.as_view()),
    path('<int:id>', ListModelDetailView.as_view()),
    # path('<int:id>/tasks', ListModelDetailView.as_view()),
]


# from .tests import *
# from .Serializers import *