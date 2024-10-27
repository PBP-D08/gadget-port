from django.urls import path
from .views import view_profile, edit_profile, add_bio, edit_bio, delete_bio, checkout_history
app_name = 'user'

urlpatterns = [
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/add_bio/', add_bio, name='add_bio'),
    path('profile/edit_bio/', edit_bio, name='edit_bio'),
    path('profile/delete_bio/', delete_bio, name='delete_bio'),  # Ensure this is defined
    path('profile/checkout_history/', checkout_history, name='checkout_history'),
]
