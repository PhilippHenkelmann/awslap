from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from recipes.views import recipe_list_view, recipe_detail_view, add_recipe_view, delete_recipe_view
from romancooking.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('recipes/', recipe_list_view, name='recipe_list'),
    path('recipes/<int:id>/', recipe_detail_view, name='recipe_detail'),
    path('recipes/add/', add_recipe_view, name='add_recipe'),
    path('recipes/delete/<int:id>/', delete_recipe_view, name='delete_recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)