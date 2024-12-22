from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    # Original views (HTML)
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/add_bio/', add_bio, name='add_bio'),
    path('profile/edit_bio/', edit_bio, name='edit_bio'),
    path('profile/delete_bio/', delete_bio, name='delete_bio'),
    path('profile/checkout_history/', checkout_history, name='checkout_history'),
    
    # JSON views (for Flutter and others)
    path('profile/json/', show_json, name='show_json'),  # For general JSON access
     path('api/edit-profile/json', edit_profile_json, name='edit_profile_json'),
    path('api/add-bio/json', add_bio_json, name='add_bio_json'),
    path('api/edit-bio/json', edit_bio_json, name='edit_bio_json'),
    path('api/delete-bio/json', delete_bio_json, name='delete_bio_json'),

    path('api/logout/jsonn', logout, name='logout'),

]
