from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('books', viewset=views.BookList)

urlpatterns = [
    path('', include(router.urls))
]