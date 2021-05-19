from rest_framework.routers import DefaultRouter

from core.api.viewsets.auth_viewset import AuthViewSet
from core.api.viewsets.user_viewset import UserViewSet
from person.api.viewset import PersonViewSet

router = DefaultRouter()

BASE_PATH_MODULE = 'core/'

router.register(r'{}person'.format(BASE_PATH_MODULE), PersonViewSet, basename='person')
router.register(r'{}user'.format(BASE_PATH_MODULE), UserViewSet, basename='user')
router.register(r'auth', AuthViewSet, basename='auth')
