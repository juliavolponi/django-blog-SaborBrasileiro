from . import views
from django.urls import path



urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipe_list'),  # Home page for listing recipes
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),  # Detail page for a single recipe
    path('new/', views.recipe_create, name='recipe_create'),  # Page for creating a new recipe
    path('recipe/<slug:slug>/update/', views.recipe_update, name='recipe_update'),  # Page for editing a recipe
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),  # Page for deleting a recipe
    path('signup/', views.signup_view, name='signup'),  
]