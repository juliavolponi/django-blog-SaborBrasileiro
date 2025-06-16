from django.contrib import admin
from .models import Recipe, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'ingredients', 'instructions')
    search_fields = ['title']
    list_filter = ('instructions',)
    prepopulated_fields = {'ingredients': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Category)
