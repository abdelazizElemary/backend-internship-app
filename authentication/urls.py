from django.urls import path, include
from .views import SignUpAPI, SignInAPI, MainUser
from knox import views as knox_views

urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/auth/register/', SignUpAPI.as_view()),
    path('api/auth/login/', SignInAPI.as_view()),
    path('api/auth/user/', MainUser.as_view()),
    path('api/auth/logout/',knox_views.LogoutView.as_view(), name="knox-logout"),
]