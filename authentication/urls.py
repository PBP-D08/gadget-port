from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('login_flutter/', login_flutter, name='login_flutter'),
    path('reg_flutter/', register_flutter, name='reg_flutter'),
    path('api/logout/json', logout, name='logout'),

]