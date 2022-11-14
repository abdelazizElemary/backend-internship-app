from django.urls import path
from knox import views as knox_views

from .views import login_view, user_profile_view, Signup_view, user_change_password_view

urlpatterns = [
    path('login/', login_view),
    path('profile/', user_profile_view),
    path('logout/', knox_views.LogoutView.as_view()),
    path('signup/', Signup_view),
    path('change-password/', user_change_password_view),

]
"""".venv
pycache 
.env
.sql
Abdelaziz Elemary8:39 PM
.gitignore"""
