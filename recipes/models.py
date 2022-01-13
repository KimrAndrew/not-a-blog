from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Ingredient(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    
    def __str__(self):
        return self.title