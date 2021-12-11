from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    #por default general un primary key que va sumando 1 
    name = models.CharField(max_length=40)
    last_name = CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    GENDER = [("H", "Hombre"),("M", "Mujer"),("N", "No especificado")]
    gender = models.CharField(max_length=1, choices=GENDER)
    key = models.CharField(max_length=40, null=False, blank=False)
    type = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

class Zona(models.Model):
    #""" Define la tabla Zona """
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nombre)

class Tour(models.Model):
    """ Define la tabla Tour """
    name = models.CharField(max_length=145)
    slug = models.CharField(max_length=45, null=True, blank=True)
    operator = models.CharField(max_length=45, null=True, blank=True)
    type = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=256)
    img = models.CharField(max_length=256, null=True, blank=True)
    pais = models.CharField(max_length=45, null=True, blank=True)
    zonaSalida = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True, blank=True, related_name="tours_salida")
    zonaLlegada = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True, blank=True, related_name="tours_llegada")

    def __str__(self):
        return "{}".format(self.name)

class Salida(models.Model):
    """ Define la tabla Salida """
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    asientos = models.PositiveSmallIntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tour = models.ForeignKey(Tour, related_name="salidas", on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}, {})".format(self.tour, self.fechaInicio, self.fechaFin)


