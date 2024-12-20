from django.urls import path
# from .views import (
#     view_profile, edit_profile, add_bio, edit_bio, delete_bio, checkout_history,
#     view_profile_flutter, edit_profile_flutter, add_bio_flutter, edit_bio_flutter, delete_bio_flutter, checkout_history_flutter,
#     show_json
# )
from .views import *

app_name = 'user'

urlpatterns = [
    # Original views
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/add_bio/', add_bio, name='add_bio'),
    path('profile/edit_bio/', edit_bio, name='edit_bio'),
    path('profile/delete_bio/', delete_bio, name='delete_bio'),  # Ensure this is defined
    path('profile/checkout_history/', checkout_history, name='checkout_history'),
    path('profile/json/', show_json, name='show_json'),
    
    # Flutter-specific views
    path('profile/view/', view_profile_flutter, name='view_profile_flutter'),
    path('profile/edit/', edit_profile_flutter, name='edit_profile_flutter'),
    path('profile/add_bio/', add_bio_flutter, name='add_bio_flutter'),
    path('profile/edit_bio/', edit_bio_flutter, name='edit_bio_flutter'),
    path('profile/delete_bio/', delete_bio_flutter, name='delete_bio_flutter'),
    path('profile/checkout_history/', checkout_history_flutter, name='checkout_history_flutter'),
    # path('profile/json/', show_json_flutter, name='show_json_flutter'),
]
