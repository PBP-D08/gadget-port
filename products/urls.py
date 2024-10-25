from django.urls import path
from products.views import show_products
from . import views

app_name = 'products'

urlpatterns = [
    path('', show_products, name='show_products'),
    path('products/', views.show_products, name='show_products'),
]