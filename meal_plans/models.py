from django.db import models
from django.conf import settings

# Create your models here.

USER_MODEL = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(null=True)
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="meal_plans",
        on_delete=models.CASCADE,
        null=True,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")

    def __str__(self):
        return self.name
