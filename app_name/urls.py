from django.urls import path

from app_name.views import MealPlanView

urlpatterns = [path("", MealPlanView.as_view(), name="meal_plans_list")]
