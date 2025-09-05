from rest_framework import serializers
from .models import Paciente, PlanoSaude

class PlanoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoSaude
        fields = ['id', 'nome']

class PacienteSerializer(serializers.ModelSerializer):
    plano = PlanoSaudeSerializer(read_only=True)

    plano_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanoSaude.objects.all(),
        source='plano',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Paciente
        fields = [
            'id',
            'nome',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'email',
            'possui_plano_saude',
            'plano',       
            'plano_id',    
        ]
