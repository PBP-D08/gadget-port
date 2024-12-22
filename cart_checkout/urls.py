from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter
# from .views import CartViewSet

# router = DefaultRouter()
# router.register(r'cart', CartViewSet, basename='cart')

app_name = 'cart_checkout'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-address/', views.update_address, name='update_address'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('json/', views.get_json_cart, name='get_json_cart'),
    path('json/details/', views.show_json_cart, name='show_json_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
]