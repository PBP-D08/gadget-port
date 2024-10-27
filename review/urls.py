from django.urls import path
from authentication.views import *
from .views import *

app_name = 'review'

urlpatterns = [
    path('product/<int:id>/', show_product_reviews, name='product_reviews'),
    path('product/<int:id>/add/', add_review, name='add_review'),
    path('review/<int:id>/delete/', delete_review, name='delete_review'),
    path('show-json/', show_json, name='show_json'),  # Menampilkan semua review dalam format JSON
# urls.py
    path('product/<int:id>/reviews/', get_product_reviews, name='get_product_reviews'),

    path('get-product-review/<int:id>/', get_product_review_by_id, name='get_product_review_by_id'),  # Mendapatkan produk berdasarkan ID
    path('delete-review/<int:id>/', delete_review, name='delete_review'),  # Menghapus review berdasarkan ID
    path('get-product-review-json/<int:id>/', get_product_review_json, name='get_product_review_json'),  # Mendapatkan review buku dalam format JSON
    path('get-user-review/<int:id>/', get_user_review, name='get_user_review'),  # Mendapatkan review pengguna berdasarkan produk
]