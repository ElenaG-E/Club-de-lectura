from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    portada_url = models.URLField(blank=True)  # Para usar imágenes de Google Books
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo

class Club(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, related_name="mis_clubes", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Club: {self.nombre} - {self.libro.titulo}"