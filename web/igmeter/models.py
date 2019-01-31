from django.db import models

# Create your models here.
#autor, titulo, comentarios y descripcion optativa.

# class Autor(models.Model):
#     idAutor = models.AutoField(primary_key=True)
#     nombre = models.TextField(max_length=100)
#     def __str__(self):
#         return 'Autor: '+self.nombre

class Resultados(models.Model):
    idResultado = models.AutoField(primary_key=True)    
    contenido = models.TextField(max_length=280)
 
    def __str__(self):
        return 'id: '+ self.idResultado+ ': ' + self.contenido


