from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', BookDetail.as_view()),
    path('', ListBook.as_view()),
    path('create', BookCreate.as_view()),
    path('delete/<int:pk>/', BookDetail.as_view()),
    path('update/<int:pk>/', BookDetail.as_view()),
]
