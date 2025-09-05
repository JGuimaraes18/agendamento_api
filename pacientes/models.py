from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.TextField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    possui_plano_saude = models.BooleanField(default=False)
    nome_plano_saude = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
