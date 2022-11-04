from rest_framework import routers
from .views import BookList
from django.urls import path, include

router = routers.DefaultRouter()
router.register('books', viewset=BookList)

urlpatterns = [
    path('', include(router.urls))
]