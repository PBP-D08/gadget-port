from django.urls import path, include
from wishlist import views

app_name = 'wishlist'

urlpatterns = [
    path('', include('user.urls')),
    path('', views.user_wishlist, name='user_wishlist'),
    path('get-wishlist-all/', views.get_wishlist_json, name='get_wishlist_json'),
    path('add-wishlist/<int:katalog_id>/', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:katalog_id>/', views.delete_wishlist, name='delete_wishlist'),
    path('get-user-wishlist/', views.view_json_wishlist, name='view_json_wishlist'),
    path('get-wishlist-katalog/', views.view_json_wishlist_katalog, name='view_json_wishlist_katalog'),
    path('get-wishlist-katalog/<int:id>/', views.view_json_wishlist_katalog_id, name='view_json_wishlist_katalog_id'),
]