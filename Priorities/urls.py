from django.urls import path
from .views import PriorityModelDetailsAPIView, PriorityModelListCreateAPIView

urlpatterns = [
    path('', PriorityModelListCreateAPIView.as_view()),
    path('<int:id>', PriorityModelDetailsAPIView.as_view()),
]
