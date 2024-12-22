from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.user_wishlist, name='user_wishlist'),
    path('add/<int:katalog_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:katalog_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('json/<int:id>/', views.show_json_wishlist, name='show_json_wishlist'),
    # path('move-to-cart/<int:wishlist_item_id>/', views.move_to_cart, name='move_to_cart'),
]