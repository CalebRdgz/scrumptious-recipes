from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name + " by " + self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField(validators=[MaxValueValidator(20)])
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    measure = models.ForeignKey("Measure", on_delete=models.PROTECT)
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    def resize_to(ingredient, target):
        servings = ingredient.recipe.servings
        if servings is not None and target is not None:
            try:
                ratio = int(target) / servings
                return ingredient.amount * ratio
            except ValueError:
                pass
        return ingredient.amount


class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)
    food_items = models.ManyToManyField("FoodItem", blank=True)

    def __str__(self):
        return str(self.order) + ". " + self.directions


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ratings",
        on_delete=models.CASCADE,
    )


class ShoppingItem(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    food_item = models.ForeignKey("FoodItem", on_delete=models.PROTECT)

    # def create_shopping_item(request):


#     # Get the ingredient_id from the POST
#     ingredient_id = request.POST.get("ingredient_id")

#     # Get the specific ingredient from the Ingredient model
#     ingredient = Ingredient.objects.get(id=ingredient_id)

#     # Get the current user
#     user = request.user
#     try:
#         # Create the new shopping item in the database
#         ShoppingItem.objects.create(
#             food_item=ingredient.food,
#             user=user,
#         )
#     # Catch the error if its already in there
#     except IntegrityError:
#         # Don't do anything with the error
#         pass

#     # Go back to the recipe page
#     return redirect("recipe_detail", pk=ingredient.recipe.id)
