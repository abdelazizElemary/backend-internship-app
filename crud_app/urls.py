from django.urls import path
from .views import BookAPI, BookAPI_id

urlpatterns = [
    path('',BookAPI.as_view()),
    path('<int:bookID>/', BookAPI_id.as_view())
]
