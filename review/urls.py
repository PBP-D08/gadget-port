from django.urls import path
from authentication.views import *
from .views import *
from cart_checkout.views import *

app_name = 'review'

urlpatterns = [
    path('product/<int:id>/', show_product_reviews, name='product_reviews'),
    path('product/<int:id>/add/', add_review, name='add_review'),
    path('product/<int:id>/add-ajax/', add_review_ajax, name='add_review_ajax'),
    path('delete/<int:id>/', delete_review, name='delete_review'),
    path('show-json/', show_json, name='show_json'),  # Menampilkan semua review dalam format JSON
# urls.py
    path('get-product-review/<int:id>/', get_product_review_by_id, name='get_product_review_by_id'),  # Mendapatkan produk berdasarkan ID
    path('get-product-review-json/<int:product_id>/', get_product_review_json, name='get_product_review_json'),

    path('delete-review/<int:id>/', delete_review, name='delete_review'),  # Menghapus review berdasarkan ID
    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),
    path('get-review-data/<int:review_id>/', get_review_data, name='get_review_data'),

    path('product/<int:id>/reviews/', get_product_reviews, name='get_product_reviews'),  # kosong
    path('get-user-review/<int:id>/', get_user_review, name='get_user_review'),  # Mendapatkan review pengguna berdasarkan produk
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]