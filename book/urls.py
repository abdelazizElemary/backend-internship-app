from rest_framework import routers
from django.db import router
from django.urls import path, include

from book.views import BookViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
