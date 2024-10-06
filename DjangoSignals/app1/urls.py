from app1 import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('createUser', views.createUser, name='createUser')
]