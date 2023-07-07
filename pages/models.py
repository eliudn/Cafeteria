from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model ):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class  Meta:
        # db_table = ''
        #  managed = True
        verbose_name = 'pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['-created']


    def __str__(self):
        return self.title