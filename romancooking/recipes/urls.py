from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list_view, name='recipe_list'),
    path('<int:id>/', views.recipe_detail_view, name='recipe_detail'),
    path('add/', views.add_recipe_view, name='add_recipe'),  # Neue URL für das Hinzufügen von Rezepten
    path('<int:id>/delete/', views.delete_recipe_view, name='delete_recipe'),
]
