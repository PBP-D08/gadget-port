from django.urls import path
from authentication.views import *
from .views import *

app_name = 'review'

urlpatterns = [
    path('detail-product/<int:id>/', show_product_admin, name='product_admin'),

    path('product/<int:id>/', show_product_reviews, name='product_reviews'),
    path('product/<int:id>/add/', add_review, name='add_review'),
    path('delete/<int:id>/', delete_review, name='delete_review'),
    path('json/', show_json, name='show_json'),  # Menampilkan semua review dalam format JSON
# urls.py
    path('get-product-review/<int:id>/', get_product_review_by_id, name='get_product_review_by_id'),  # Mendapatkan produk berdasarkan ID
    path('get-product-review-json/<int:product_id>/', get_product_review_json, name='get_product_review_json'),

    path('delete-review/<int:id>/', delete_review, name='delete_review'),  # Menghapus review berdasarkan ID
    path('delete-review-admin/<int:review_id>/', delete_review_admin, name='delete_review_admin'),  # Admin Menghapus review 

    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),
    path('get-review-data/<int:review_id>/', get_review_data, name='get_review_data'),

    path('user_product/<int:id>/', show_product_reviews, name='store_product_reviews'),
    path('admin_product/<int:id>/', show_product_admin, name='store_product_admin'),
]