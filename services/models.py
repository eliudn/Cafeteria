from django.db import models

class Service(models.Model):
    title=  models.CharField(max_length=200, verbose_name="Titulo")
    subtitle =   models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField( verbose_name="Imgen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class  Meta:
        # db_table = ''
        #  managed = True
        verbose_name = 'servico'
        verbose_name_plural = 'servicios'
        ordering = ['-created']
    def __str__(self):
        return self.title
