from django.urls import path

from .views import RegisterStudentView

app_name = 'users'
urlpatterns = [
    path('register/', RegisterStudentView.as_view(), name="register_student"),
]