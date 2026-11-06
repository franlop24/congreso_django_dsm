from django.urls import path

from . import views

app_name = "workshops"
urlpatterns = [
    path('', views.workshop_list, name="workshop_list"),
]