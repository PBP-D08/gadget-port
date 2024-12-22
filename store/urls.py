from django.urls import path
from store.views import add_store_flutter, edit_store_flutter, get_product_by_id, get_store_json, list_store, delete_store_flutter
from . import views

app_name = 'store'

urlpatterns = [
    path('list_store/', views.list_store, name='list_store'),
    path('add_store/', views.add_store, name='add_store'),
    path('store_detail/<int:id>', views.store_detail, name='store_detail'),
    path('delete_store/<int:id>', views.delete_store, name='delete_store'),
    path('edit_store/<int:id>', views.edit_store, name='edit_store'),
    path('json/', views.show_json_store, name='show_json_store'),
    path('get-store-json/', get_store_json, name='get_store_json'),
    path('add-store/', add_store_flutter, name='add_store_flutter'),
    path('edit-store/<int:store_id>/', edit_store_flutter, name='edit_store_flutter'),
    path('delete-store/<int:id>/', delete_store_flutter, name='delete_store_flutter'),
    path('get-product/<int:id>/', get_product_by_id, name='get_product_by_id'),
]