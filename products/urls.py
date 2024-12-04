from django.urls import path
from products.views import show_products
from . import views

app_name = 'products'

urlpatterns = [
    path('show_products/', views.show_products, name='show_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('json/', views.get_product, name='get_product'),
    path('json/<int:id>/', views.get_product_by_id, name='get_product_by_id'),
]