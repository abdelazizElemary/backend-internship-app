from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('rest/cbv/', views.CBV_List.as_view()),
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),
    path('findbook/', views.find_book),
    path('addbook/', views.new_book),
    path('api-token-auth/', obtain_auth_token),
]