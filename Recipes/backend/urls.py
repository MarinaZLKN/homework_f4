
from django.urls import path

from backend.views import RecipeAPIView, CategoryAPIView, RecipeDetailView, CategoryDetailView

urlpatterns = [
    path('recipelist/', RecipeAPIView.as_view({'get': 'list'})),
    path('categorylist/', CategoryAPIView.as_view({'get': 'list'})),
    path('recipelist/<int:pk>/', RecipeDetailView.as_view({'get': 'retrieve'})),
    path("categorylist/<int:pk>/", CategoryDetailView.as_view({"get": "list"})),
]