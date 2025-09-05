from django.db import models
from pacientes.models import Paciente
from profissionais.models import Profissional

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)
    realizada = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tem_convenio = models.BooleanField(default=False)
    nome_convenio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} com {self.profissional} em {self.data_hora}"