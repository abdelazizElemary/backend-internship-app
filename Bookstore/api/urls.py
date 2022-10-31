from django.urls import path
from . import views

urlpatterns = [
    path('api/token/auth/', views.CustomAuthToken.as_view()),
    path('getbooks/', views.BooksList.as_view()),
    path('update/', views.UpdateList.as_view(), {'pk':None}),
    path('update/<str:pk>/', views.UpdateList.as_view()),
]