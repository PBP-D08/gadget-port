from django.urls import path
from . import views

app_name = 'cart_checkout'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update/', views.update_address, name='update_address'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
]