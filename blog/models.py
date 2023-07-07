from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
       
        verbose_name = 'Categoria'
        verbose_name_plural = 'Catergorias '
        ordering = ['-created']

    def __str__(self):
        return self.name
     
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content =models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    author = models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE)
    image = models.ImageField( verbose_name="Imgen", upload_to="blog")
    categories = models.ManyToManyField(Category, verbose_name="categorias", related_name="get_post")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
       
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title
