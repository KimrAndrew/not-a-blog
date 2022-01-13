from rest_framework import serializers
from .models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','description','protein','fat','carbs')
        model = Ingredient