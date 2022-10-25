from django.urls import path
from .views import BookList , BookDetail

urlpatterns = [
    # for list books and creat new books
    path('books/',BookList.as_view() , name='Book_list_api'),
    # for retrieve, update or delete a book
    path('book/<int:id>/',BookDetail.as_view() , name='Book_detail_api'),
]