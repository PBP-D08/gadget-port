from django.urls import path
from .views import view_profile, edit_profile, add_sub_profile

app_name = 'user'
urlpatterns = [
    path('profile/', view_profile, name='view'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/add_sub/', add_sub_profile, name='add_sub_profile'),
]
