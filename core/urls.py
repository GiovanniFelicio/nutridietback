from rest_framework.routers import DefaultRouter
from person.api.viewset import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')

