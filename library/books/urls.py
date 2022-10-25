from django.urls import include, path
from .api_views import BookListApi , BookDetail

urlpatterns = [
    # for list books and creat new books
    path('books/',BookListApi.as_view() , name='Book_list_api'),
    # for retrieve, update or delete a book
    path('book/<int:id>/',BookDetail.as_view() , name='Book_detail_api'),
]