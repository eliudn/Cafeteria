from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class  Meta:
        # db_table = ''
        #  managed = True
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['-created']


    def __str__(self):
        return self.name

