from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/', views.hello),
    path('uper/<str:name>/', views.uppercase),
    path('users/', views.users),
]