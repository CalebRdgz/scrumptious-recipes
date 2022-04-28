from typing import List
from django.shortcuts import render

from django.views.generic.list import ListView
from meal_plans.models import MealPlan

# Create your views here.


class MealPlanView(ListView):
    model = MealPlan
    template_name = "mealplans/list.html"
