from django.urls import path, include
from rest_framework.authtoken import views as auth_view

from .views import login_view, user_profile_view, Signup_view, user_change_password_view

urlpatterns = [
    path('login/', login_view),
    path('profile/', user_profile_view),
    path('signup/', Signup_view),
    path('change-password/', user_change_password_view),

]
"""".venv
pycache
.env
.sql
Abdelaziz Elemary8:39 PM
.gitignore"""
