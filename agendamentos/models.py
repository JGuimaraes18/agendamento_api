from django.db import models
from pacientes.models import Paciente
from profissionais.models import PlanoSaude, Profissional, Especialidade

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.SET_NULL, null=True, blank=True)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)
    realizada = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tem_convenio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.paciente} com {self.profissional} em {self.data_hora}"