from django.db import models

class MenuHotel(models.Model):
    titulo = models.CharField(max_length=100)

    icone = models.CharField(
        max_length=20,
        blank=True
    )

    url = models.CharField(
        max_length=200,
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    ordem = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.titulo