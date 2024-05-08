from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuarios(AbstractUser):
    id= models.AutoField(primary_key= True)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=120, null=False)
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.username

class cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=150)
    telefono = models.IntegerField()
    def __str__(self):
        return str(self.id_cliente)+' - '+str(self.nombre_empresa)

class estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=30)
    '''Dict ESTADO
        -1:Abierto
        -2:Perdido
        -3:Ganado
    '''
    def __str__(self):
        return str(self.id_estado)+' - '+self.estado

class etapa(models.Model):
    id_etapa = models.BigAutoField(primary_key=True)
    etapa = models.CharField(max_length=30)
    '''Dict ETAPA
        -1:En conservación
        -2:Conseguido
        -3:Perdido
    '''
    def __str__(self):
        return str(self.id_etapa)+ ' - '+self.etapa


class prospecto(models.Model):
    SexoFields = {
        'Male': 'Masculino',
        'Fem': 'Femenino'
    }
    id_prospecto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(auto_now=True)
    sexo = models.CharField(max_length=40,  choices=SexoFields)
    cliente_id = models.ForeignKey(cliente, on_delete=models.CASCADE)
    estado_id = models.ForeignKey(estado, on_delete=models.CASCADE)
    etapa_id = models.ForeignKey(etapa, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_prospecto)

