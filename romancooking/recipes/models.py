from django.db import models

# Erstelle deine Modelle hier.
class RomanDish(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default='Apicius')
    ingredients = models.TextField()
    preparation = models.TextField()
    historical_context = models.TextField(null=True, blank=True)
    instructions = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True) 
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)


    def __str__(self):
        return self.title
