from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.api.serializers.user_serializer import UserSerializer
from core.common.models.user import User


class UserViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        user: User = User.objects.get(pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def list(self, request, *args, **kwargs) -> Response:
        serializer = UserSerializer(User.objects.all(), many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
