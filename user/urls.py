from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('profile/', views.user_profile_view, name='user_profile'),
]