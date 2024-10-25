from django.urls import path
from authentication.views import *
from .views import *

app_name = 'review'

urlpatterns = [
    path('<int:id>/', show_main, name='show_main'),  # Menampilkan halaman utama produk
    path('add-review-ajax/<int:id>/', add_review, name='add_review'),  # Menambahkan review produk
    path('show-json/', show_json, name='show_json'),  # Menampilkan semua review dalam format JSON
    path('get-product-review/', get_product_review, name='get_product_review'),  # Mendapatkan semua produk
    path('get-product-review/<int:id>/', get_product_review_by_id, name='get_product_review_by_id'),  # Mendapatkan produk berdasarkan ID
    path('delete-review/<int:id>/', delete_review, name='delete_review'),  # Menghapus review berdasarkan ID
    path('get-product-review-json/<int:id>/', get_product_review_json, name='get_product_review_json'),  # Mendapatkan review buku dalam format JSON
    path('get-user-review/<int:id>/', get_user_review, name='get_user_review'),  # Mendapatkan review pengguna berdasarkan produk
]