#from django.shortcuts import render
from rest_framework import generics
from .models import Ingredient
from .serializers import IngredientSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
