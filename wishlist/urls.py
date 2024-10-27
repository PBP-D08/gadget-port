from django.urls import path, include
from wishlist import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.user_wishlist, name='user_wishlist'),
    path('toggle-wishlist/<int:katalog_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('add-to-wishlist/<int:katalog_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:katalog_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('move-to-cart/<int:wishlist_item_id>/', views.move_to_cart, name='move_to_cart'),
]
