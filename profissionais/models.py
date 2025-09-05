from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class PlanoSaude(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    VINCULO_CHOICES = [
        ('PJ', 'Pessoa Jurídica'),
        ('CLT', 'CLT'),
        ('HORISTA', 'Horista'),
        ('DIARISTA', 'Diarista'),
    ]

    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)

    vinculo = models.CharField(max_length=10, choices=VINCULO_CHOICES)
    cnpj = models.CharField(max_length=18, blank=True, null=True, unique=True) 

    especialidades = models.ManyToManyField(Especialidade, related_name="profissionais")
    planos_saude = models.ManyToManyField(PlanoSaude, blank=True, related_name="profissionais")

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
