from rest_framework import serializers
from .models import Consulta
from pacientes.models import Paciente
from profissionais.models import Profissional, Especialidade, PlanoSaude

class ConsultaSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
        source="paciente",
        queryset=Paciente.objects.all(),
        write_only=True,
        label="Paciente"
    )
    profissional_id = serializers.PrimaryKeyRelatedField(
        source="profissional",
        queryset=Profissional.objects.all(),
        write_only=True,
        label="Profissional"
    )
    especialidade_id = serializers.PrimaryKeyRelatedField(
        source="especialidade",
        queryset=Especialidade.objects.all(),
        write_only=True,
        label="Especialidade"
    )
    plano_id = serializers.PrimaryKeyRelatedField(
        source="plano",
        queryset=PlanoSaude.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
        label="Plano de Saúde"
    )

    paciente_nome = serializers.CharField(source="paciente.nome", read_only=True)
    profissional_nome = serializers.CharField(source="profissional.nome", read_only=True)
    especialidade_nome = serializers.CharField(source="especialidade.nome", read_only=True)
    plano_nome = serializers.CharField(source="plano.nome", read_only=True)

    class Meta:
        model = Consulta
        fields = [
            "id",
            "paciente_id", "paciente_nome",
            "profissional_id", "profissional_nome",
            "especialidade_id", "especialidade_nome",
            "plano_id", "plano_nome",
            "tem_convenio",
            "data_hora",
            "realizada",
            "observacoes",
            "valor",
        ]
