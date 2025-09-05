from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet)

urlpatterns = router.urls