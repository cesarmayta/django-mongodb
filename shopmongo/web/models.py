#from django.db import models
from djongo import models
# Create your models here.
class Categoria(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    @property
    def pk(self):
        return self._id

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    @property
    def pk(self):
        return self._id

    def __str__(self):
        return self.nombre