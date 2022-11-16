import knox.views as knox_views
from .views import LoginView, RegistrationView
from django.urls import path, include

urlpatterns = [
    # path('', include('knox.urls')),
    path('login/', LoginView.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('register/', RegistrationView.as_view()),
]
