from django.urls import path

from meal_plans.views import MealPlanView

urlpatterns = [
    path("meal_plans/", MealPlanView.as_view(), name="meal_plans_list"),
    # path("meal_plans/", MealPlanView.as_view(), name="meal_plans_list"),
    # path("meal_plans/", MealPlanView.as_view(), name="meal_plans_list"),
    # path("meal_plans/", MealPlanView.as_view(), name="meal_plans_list"),
    # path("meal_plans/", MealPlanView.as_view(), name="meal_plans_list"),
]
