from rest_framework import viewsets
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all().order_by('data_hora')
    serializer_class = ConsultaSerializer