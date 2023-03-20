
from django.urls import path

from backend.views import RecipeAPIView, CategoryAPIView

urlpatterns = [
    path('recipelist/', RecipeAPIView.as_view()),
    path('categorylist/', CategoryAPIView.as_view()),
]