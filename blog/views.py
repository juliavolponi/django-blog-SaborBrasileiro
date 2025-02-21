# from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6



class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  
    model = Recipe
    template_name = "blog/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        """Ensure only the author can delete the recipe"""
        recipe = self.get_object()
        return self.request.user == recipe.author 
    



def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    recipe = get_object_or_404(Recipe, slug=slug)

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe},
    )


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # author logged-in user
            recipe.save()
            # Redirect the user to the recipe detail view of the created recipe
            return redirect('recipe_list')
    else:
        # If the request method is not POST, create an empty form
        form = RecipeForm()
        # renders the template for the recipe creation form so it can be displayed for user
    return render(request, 'blog/recipe_form.html', {'form': form})


@login_required
def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    # Check if the current user is the author of the recipe
    if request.user != recipe.author:
        # If not the author, redirect to the recipe detail page
        return redirect('recipe_list')

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            # Redirect to the recipe detail page after successful update
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'blog/recipe_form.html', {'form': form})


# user authentication

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')  # Redirect to recipe list after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



