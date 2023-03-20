from rest_framework import generics
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer


class RecipeAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



