from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_cooked')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ('name',)


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'weight')
