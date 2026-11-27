from django.contrib.auth.forms import UserCreationForm

from .models import Student

class RegisterStudentForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name', 'enrollment')