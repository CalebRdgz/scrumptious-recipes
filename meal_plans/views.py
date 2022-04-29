from django.shortcuts import render
from typing import List
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from meal_plans.models import MealPlan

# Create your views here.


class MealPlanListView(ListView):
    model = MealPlan
    template_name = "mealplans/list.html"
    paginate_by = 2


class MealPlanCreateView(CreateView):
    model = MealPlan
    template_name = "mealplans/new.html"


class MealPlanDetailView(DetailView):
    model = MealPlan
    template_name = "mealplans/detail.html"


class MealPlanUpdateView(UpdateView):
    model = MealPlan
    template_name = "mealplans/edit.html"


class MealPlanDeleteView(DeleteView):
    model = MealPlan
    template_name = "mealplans/delete.html"
