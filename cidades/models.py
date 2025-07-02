from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nome}'

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome}'

class SeuModelo(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cidade} - {self.estado}"