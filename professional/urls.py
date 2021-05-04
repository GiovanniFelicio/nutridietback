from rest_framework.routers import DefaultRouter
from .api.viewset import ProfessionalViewSet

router = DefaultRouter()
router.register(r'professional', ProfessionalViewSet, basename='professional')

