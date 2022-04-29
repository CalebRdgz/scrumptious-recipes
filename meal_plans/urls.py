from django.urls import path

from meal_plans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanUpdateView,
    MealPlanDetailView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plans_list"),
    path(
        "/create/",
        MealPlanCreateView.as_view(),
        name="meal_plans_create",
    ),
    path(
        "meal_plans/<int:pk>",
        MealPlanDetailView.as_view(),
        name="meal_plans_detail",
    ),
    path(
        "meal_plans/<int:pk>/edit/",
        MealPlanUpdateView.as_view(),
        name="meal_plans_Update",
    ),
    path(
        "meal_plans/<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plans_delete",
    ),
]
