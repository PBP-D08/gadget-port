from django.urls import path
from main.views import show_main
from cart_checkout.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
]