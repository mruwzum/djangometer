from django.db import models

# Create your models here.
#autor, titulo, comentarios y descripcion optativa.

class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=100)
    def __str__(self):
        return 'Autor: '+self.nombre

class Noticias(models.Model):
    idNoticia = models.AutoField(primary_key=True)    
    titulo = models.TextField(max_length=100)
    link = models.TextField(max_length=200)
    autor = models.TextField(max_length=100)
    comentarios = models.BigIntegerField(blank=False,default=0)
    fecha = models.DateField(auto_now=True)
 
    def __str__(self):
        return 'Noticia: '+ self.titulo+ 'Enlace: ' + self.link+ 'Autor: '+self.autor+ 'Comentarios'+str(self.comentarios)+ 'Fecha: '+str(self.fecha)


