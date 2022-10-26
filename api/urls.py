from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('add/book/', views.add_book, name='add-book'),
    path('all/', views.view_books, name='view-books'),
]
