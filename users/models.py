from django.db import models
from django.contrib.auth.models import User

from workshops.models import Workshop

class Student(User):
    enrollment = models.CharField("Matrícula", max_length=11)
    folio = models.CharField(
        "Fólio", 
        max_length=4, 
        null=True, blank=True, unique=True)
    is_valid = models.BooleanField(
        "Es Válida?", default=False)
    workshop = models.ForeignKey(
        Workshop, related_name="students",
        on_delete=models.SET_NULL, verbose_name="Taller",
        null=True, blank=True)

    def __str__(self):
        return self.enrollment + " " + self.get_full_name()
    

class Tutor(User):
    pass

class Instructor(User):
    pass