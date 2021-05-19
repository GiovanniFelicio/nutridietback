from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include

from core.urls import router as core_router
from patient.urls import router as patient_router
from professional.urls import router as professional_router


router = routers.DefaultRouter()
router.registry.extend(core_router.registry)
router.registry.extend(patient_router.registry)
router.registry.extend(professional_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
