from unittest import TestCase

from recipes.models import Ingredient, Recipe
from recipes.templatetags.resizer import resize_to


class ResizeToTests(TestCase):
    def test_recipe_has_no_serving(self):
        # Arrange
        print("Serving size should stay the same when target is none.")
        recipe = Recipe(servings=None)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, None)

        # Assert
        self.assertEqual(5, result)

    def test_values_for_servings_amount_and_target(self):
        # Arrange
        print("Should resize to the correct amount.")
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, 10)

        # Assert
        self.assertEqual(25, result)

    # def test_target_is_letters(self):
    #     # Arrange

    #     # Act

    #     # Assert
