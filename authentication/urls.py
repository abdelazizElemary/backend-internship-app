from django.urls import path
from . import views
from knox.views import LogoutView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view() , name = 'login'),
    path('logout/', LogoutView.as_view() , name = 'logout')
]   