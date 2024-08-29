from django import forms
from .models import RomanDish

class RomanDishForm(forms.ModelForm):
    class Meta:
        model = RomanDish
        fields = ['title', 'ingredients', 'preparation', 'historical_context', 'instructions', 'image', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
