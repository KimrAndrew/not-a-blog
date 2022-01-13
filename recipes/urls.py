from django.urls import path
from .views import IngredientList, IngredientDetail

urlpatterns = [
    path('',IngredientList.as_view(), name='recipe_list'),
    path('<int:pk>/', IngredientDetail.as_view(),name='recipe_detail')
]