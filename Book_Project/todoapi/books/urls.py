from rest_framework import routers
from . import views 
from django.urls import path, include 

from .views import RegisterAPI
from django.urls import path


router = routers.DefaultRouter()

router.register('books', viewset=views.BooksList)

urlpatterns = [
    path('', include(router.urls)),
 
]
]
