from django.urls import path
from .views import TaskModelDetailsAPIView, TaskModelListAPIView

urlpatterns = [
    path('', TaskModelListAPIView.as_view()),
    path('<int:id>', TaskModelDetailsAPIView.as_view()),
]


# from .tests import *