from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    local = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
