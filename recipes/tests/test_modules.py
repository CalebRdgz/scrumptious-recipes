# from lib2to3.pgen2.literals import test
# from unittest import TestCase

# from psycopg2 import IntegrityError
# from recipes.models import FoodItem, Measure
# from django.db import IntegrityError

# Measure.objects.filter(name="pint").delete()
# Measure.objects.filter(name="ounce").delete()

# Measure.objects.filter(name="ounce", abbreviation="o")
# Measure.objects.create(name="pint", abbreviation="p")


# class FoodItemTestCorrectLength(TestCase):
#     def test_name_correct_length(self):
#         FoodItem.objects.create(name="grape")
#         print(
#             "Should be able to add a good item with a name under 100 chars"
#         )
#         test_food_item = FoodItem.objects.get(name="grape")
