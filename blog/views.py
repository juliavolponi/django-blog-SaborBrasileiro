# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Create a new recipe instance without saving it to the database yet
            recipe = form.save(commit=False)
            recipe.author = request.user  # author logged-in user
            recipe.save()
            # Redirect the user to the recipe detail view of the created recipe
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        # If the request method is not POST, create an empty form
        form = RecipeForm()
        # renders the template for the recipe creation form so it can be displayed for user
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # Check if the current user is the author of the recipe
    if request.user != recipe.author:
        # If not the author, redirect to the recipe detail page
        return redirect('recipe_detail', pk=recipe.pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            # Redirect to the recipe detail page after successful update
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user == recipe.author:
        recipe.delete()
    return redirect('recipe_list')



