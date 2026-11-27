from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import RegisterStudentForm

class RegisterStudentView(CreateView):
    form_class = RegisterStudentForm
    template_name = "users/register_student.html"
    success_url = reverse_lazy('home')