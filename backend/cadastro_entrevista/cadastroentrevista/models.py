from django.db import models

class Usuario(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=10)



    class Meta:
        ordering = ['created']