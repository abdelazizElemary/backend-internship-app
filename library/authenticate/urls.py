from django.urls import path
from .views import Register, Login, Logout
from knox import views as knox_views

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]