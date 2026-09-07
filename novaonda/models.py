from django.db import models
models.ImageField

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

    

class Suite(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField(
        blank=True
    )

    capacidade = models.PositiveIntegerField(
        default=1
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    imagem = models.ImageField(
        upload_to='suites/',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    ordem = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.nome


class Foto(models.Model):

    titulo = models.CharField(
        max_length=100
    )

    descricao = models.TextField(
        blank=True
    )

    imagem = models.ImageField(
        upload_to='galeria/',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    ordem = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.titulo