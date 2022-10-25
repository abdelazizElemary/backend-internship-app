from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.getBooks),
    path('addbook/', views.addBooks),
    path('deletebook/<str:pk>/', views.deleteBook),
    path('updatebook/<str:pk>/', views.updateBook),
]