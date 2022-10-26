from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('add/book/', views.add_book, name='add-book'),
    path('all/', views.view_books, name='view-books'),
    path('update/book/<int:pk>/', views.update_book, name='update-items'),
    path('delete/book/<int:pk>/', views.delete_book, name='delete-items'),
]
