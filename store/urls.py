from django.urls import path
from store.views import list_store
from . import views

app_name = 'store'

urlpatterns = [
    path('list_store/', views.list_store, name='list_store'),
    path('add_store/', views.add_store, name='add_store'),
    path('store_detail/<int:id>', views.store_detail, name='store_detail'),
    path('delete_store/<int:id>', views.delete_store, name='delete_store'),
    path('edit_store/<int:id>', views.edit_store, name='edit_store'),
]