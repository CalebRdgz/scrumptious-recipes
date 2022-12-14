from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipeListView,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    # path(
    #     "shopping_items/create/",  # This is the pattern that
    #     # Django uses to match URLs
    #     # when someone makes a request
    #     create_shopping_item,  # This is the function that is
    #     # called when the URL matches
    #     # recipes/shopping_items/create/
    #     name="shopping_item_create"  # This is the name that we use
    #     # in redirect, reverse, and
    #     # {% url %} tags
    # ),
]
