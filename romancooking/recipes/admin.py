from django.contrib import admin
from .models import RomanDish

@admin.register(RomanDish)
class RomanDishAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ingredients', 'preparation')
