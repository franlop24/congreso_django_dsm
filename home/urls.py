from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('uper/<str:name>/', views.uppercase, name='mayus'),
    path('users/', views.users, name='users'),
]