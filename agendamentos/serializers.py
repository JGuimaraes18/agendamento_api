from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
        source="paciente",
        queryset=Consulta._meta.get_field("paciente").remote_field.model.objects.all(),
        write_only=True,
        label="Paciente"
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
            "profissional_nome",
            "especialidade_nome",
            "plano_nome",
            "tem_convenio",
            "data_hora",
            "realizada",
            "observacoes",
            "valor",
        ]
