from rest_framework import viewsets
from .models import Profissional, Especialidade, PlanoSaude
from .serializers import ProfissionalSerializer, EspecialidadeSerializer, PlanoSaudeSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class PlanoSaudeViewSet(viewsets.ModelViewSet):
    queryset = PlanoSaude.objects.all()
    serializer_class = PlanoSaudeSerializer
