from rest_framework.decorators import action, authentication_classes
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from core.common.models import User


@authentication_classes([])
@permission_classes([])
class AuthViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    @action(methods=['POST'], url_path="login", detail=False)
    def login(self, request):
        user: User = get_user_model()

        username = request.data.get('username')
        password = request.data.get('password')

        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong password')

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token)
        })
