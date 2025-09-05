from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profissionais', views.ProfissionalViewSet)
router.register(r'especialidades', views.EspecialidadeViewSet)
router.register(r'planos', views.PlanoSaudeViewSet)

urlpatterns = router.urls