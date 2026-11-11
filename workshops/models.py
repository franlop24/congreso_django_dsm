from django.db import models

# Create your models here.
# un modelo es una representación de una tabla
# ORM donde una tabla es una clase (atributos, métodos)

class Classroom(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", null=True, blank=True)
    building = models.CharField("Edificio", max_length=100)

    FLOORS = [("planta_baja", "Planta Baja"), ("planta_alta", "Planta Alta")]
    floor = models.CharField("Planta", max_length=50, choices=FLOORS)

    def __str__(self):
        return self.name + " - " + self.building

    class Meta:
        verbose_name = "Salón/Laboratorio"
        verbose_name_plural = "Salones/Laboratorios"


class Instructor(models.Model):
    pass

class Workshop(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción")
    # instructor = models.CharField("Instructor", max_length=100)
    capacity = models.IntegerField("Capacidad")
    classroom = models.ForeignKey(Classroom, 
                                related_name="workshops", 
                                on_delete=models.SET_NULL,
                                null=True, blank=True)
    image = models.ImageField("Imagen de Taller", 
                              upload_to="images",
                              null=True, blank=True)
    date = models.DateField("Fecha")
    start_time = models.TimeField("Hora de inicio")
    end_time = models.TimeField("Hora de termino")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"