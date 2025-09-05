from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pacientes.urls')),
    path('api/', include('profissionais.urls')),
    path('api/', include('agendamentos.urls')),
]
