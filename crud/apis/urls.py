from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'authors', views.AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
