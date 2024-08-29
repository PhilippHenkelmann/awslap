from django.shortcuts import render, get_object_or_404, redirect
from .models import RomanDish
from .forms import RomanDishForm

def recipe_list_view(request):
    recipes = RomanDish.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail_view(request, id):
    recipe = get_object_or_404(RomanDish, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe_view(request):
    if request.method == 'POST':
        form = RomanDishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RomanDishForm()
    return render(request, 'add_recipe.html', {'form': form})

def delete_recipe_view(request, id):
    recipe = get_object_or_404(RomanDish, id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'delete_recipe.html', {'recipe': recipe})
