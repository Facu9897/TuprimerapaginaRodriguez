from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo    = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.titulo

class Comentario(models.Model):
    post     = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre   = models.CharField(max_length=100)
    email    = models.EmailField()
    contenido = models.TextField()
    fecha    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"Comentario de {self.nombre} en {self.post}"

