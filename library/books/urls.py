from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views
from . import views
router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router1.register(r'user', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('user/', include(router1.urls)),
]