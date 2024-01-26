from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Recipe, Product, RecipeProduct


@require_http_methods(["GET", "POST"])
def add_product_to_recipe(request):
    if request.method == 'POST':
        try:
            recipe_id = request.POST.get('recipe_id')
            product_id = request.POST.get('product_id')
            weight = request.POST.get('weight')

            recipe = Recipe.objects.get(id=recipe_id)
            product = Product.objects.get(id=product_id)

            recipe_product, created = RecipeProduct.objects.update_or_create(
                recipe=recipe, product=product, defaults={'weight': weight}
            )

            return JsonResponse({
                "status": "success",
                "message": f"Product {product.name} added to {recipe.name} with weight {weight}g."
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return render(request, 'add_product_to_recipe.html')


@require_http_methods(["GET", "POST"])
def cook_recipe(request):
    if request.method == 'POST':
        try:
            recipe_id = request.POST.get('recipe_id')
            recipe = Recipe.objects.get(id=recipe_id)

            for product in recipe.products.all():
                product.times_cooked += 1
                product.save()

            return JsonResponse({
                "status": "success",
                "message": f"Recipe {recipe.name} cooked successfully."
            })
        except Recipe.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Recipe not found."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:

        return render(request, 'cook_recipe.html')


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    recipes = Recipe.objects.exclude(
        products__id=product_id,
        recipeproduct__weight__gte=10
    )
    return render(request, 'show_recipes_without_product.html', {'recipes': recipes})
