from rest_framework import serializers
from .models import Profissional, Especialidade, PlanoSaude


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']


class PlanoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoSaude
        fields = ['id', 'nome']


class ProfissionalSerializer(serializers.ModelSerializer):
    especialidades = EspecialidadeSerializer(many=True, read_only=True)
    planos_saude = PlanoSaudeSerializer(many=True, read_only=True)

    especialidades_ids = serializers.PrimaryKeyRelatedField(
        queryset=Especialidade.objects.all(), many=True, write_only=True, required=False
    )
    planos_saude_ids = serializers.PrimaryKeyRelatedField(
        queryset=PlanoSaude.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = Profissional
        fields = [
            'id',
            'nome',
            'email',
            'telefone',
            'vinculo',
            'cnpj',
            'ativo', 
            'especialidades',
            'planos_saude',
            'especialidades_ids',
            'planos_saude_ids',
        ]

    def create(self, validated_data):
        especialidades = validated_data.pop('especialidades_ids', [])
        planos = validated_data.pop('planos_saude_ids', [])
        profissional = Profissional.objects.create(**validated_data)
        profissional.especialidades.set(especialidades)
        profissional.planos_saude.set(planos)
        return profissional

    def update(self, instance, validated_data):
        especialidades = validated_data.pop('especialidades_ids', None)
        planos = validated_data.pop('planos_saude_ids', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if especialidades is not None:
            instance.especialidades.set(especialidades)
        if planos is not None:
            instance.planos_saude.set(planos)

        return instance
