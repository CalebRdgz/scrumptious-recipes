from django.contrib import admin
from recipes.models import Recipe


# Register your models here.
# ModelAdmin is already in django (it comes with django)
class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
