from rest_framework import serializers
from .models import Consulta
from pacientes.serializers import PacienteSerializer
from profissionais.serializers import ProfissionalSerializer, EspecialidadeSerializer, PlanoSaudeSerializer

class ConsultaSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    profissional = ProfissionalSerializer(read_only=True)
    especialidade = EspecialidadeSerializer(read_only=True)
    plano = PlanoSaudeSerializer(read_only=True) 

    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=PacienteSerializer.Meta.model.objects.all(),
        source='paciente',
        write_only=True,
        label="Paciente"
    )
    profissional_id = serializers.PrimaryKeyRelatedField(
        queryset=ProfissionalSerializer.Meta.model.objects.all(),
        source='profissional',
        write_only=True,
        label="Profissional"
    )
    especialidade_id = serializers.PrimaryKeyRelatedField(
        queryset=EspecialidadeSerializer.Meta.model.objects.all(),
        source='especialidade',
        write_only=True,
        label="Especialidade" 
    )
    plano_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanoSaudeSerializer.Meta.model.objects.all(),
        source='plano',
        write_only=True,
        required=False,
        allow_null=True,
        label="Nome do Plano" 
    )

    tem_convenio = serializers.BooleanField(label="Plano de Saúde", required=False)

    class Meta:
        model = Consulta
        fields = [
            'id',
            'paciente', 'paciente_id',
            'profissional', 'profissional_id',
            'especialidade', 'especialidade_id',
            'tem_convenio',
            'plano', 'plano_id',
            'data_hora',
            'realizada',
            'observacoes',
            'valor',
        ]