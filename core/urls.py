from rest_framework.routers import DefaultRouter
from person.api.viewset import PersonViewSet

router = DefaultRouter()

BASE_PATH_MODULE = 'core/'

router.register(r'{}person'.format(BASE_PATH_MODULE), PersonViewSet, basename='person')

