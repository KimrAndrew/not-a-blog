from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

from .models import Ingredient

class IngredientTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1',password='pass')
        testuser1.save()

        test_ingredient = Ingredient.objects.create(
            author = testuser1,
            title = 'Cucumber',
            description = 'Vitamins, minerals, very high number',
            protein = 0,
            fat = 0,
            carbs = 3
        )

        test_ingredient.save()

    def test_recipe_content(self):
        ingredient = Ingredient.objects.get(id=1)
        actual_author = str(ingredient.author)
        actual_title = str(ingredient.title)
        actual_description = str(ingredient.description)
        actual_protein = int(ingredient.protein)
        actual_fat = int(ingredient.fat)
        actual_carbs = int(ingredient.carbs)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title,'Cucumber')
        self.assertEqual(actual_description, 'Vitamins, minerals, very high number')
        self.assertEqual(actual_protein, 0)
        self.assertEqual(actual_fat, 0)
        self.assertEqual(actual_carbs, 3)