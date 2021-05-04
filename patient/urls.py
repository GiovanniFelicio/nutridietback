from rest_framework.routers import DefaultRouter
from patient.api.viewset import PatientViewSet

router = DefaultRouter()
router.register(r'patient', PatientViewSet, basename='patient')

