from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/',knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('getbooks/', views.BooksList.as_view()),
    path('update/', views.UpdateList.as_view(), {'pk':None}),
    path('update/<str:pk>/', views.UpdateList.as_view()),
]