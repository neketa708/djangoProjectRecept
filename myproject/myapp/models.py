from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField()  # время в минутах, например
    image = models.ImageField(upload_to='recipe_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # другие поля на ваш выбор, например
    # ingredients = models.ManyToManyField(Ingredient)

class Category(models.Model):
    name = models.CharField(max_length=50)
    # другие поля на ваш выбор

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # другие поля на ваш выбор