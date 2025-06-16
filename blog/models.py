from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # comments are deleted as well if a post is deleted
    categories = models.ManyToManyField(Category, related_name="recipes")  # Many-to-Many relationship
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image')

    def save(self, *args, **kwargs):
        if not self.slug:
            # Automatically generate the slug from the title
            self.slug = slugify(self.title)

        if Recipe.objects.filter(slug=self.slug).exists():
            self.slug=f"{self.slug}-{self.id}"
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

