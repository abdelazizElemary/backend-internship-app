from django.urls import path
from rest_framework import routers

from . import views
from .views import BookViewSet

from django.urls import  path,include

router = routers.DefaultRouter()

router.register(r'', BookViewSet)

urlpatterns = [ 
    path('', include(router.urls)),

    path('create/', views.BookList.as_view(), name='create')
]