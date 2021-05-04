from rest_framework.viewsets import ViewSet
from .serializer import ProfessionalSerializer
from professional.models import Professional
from rest_framework.response import Response


class ProfessionalViewSet(ViewSet):
    queryset = Professional.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = ProfessionalSerializer(self.queryset, many=True)

        return Response(serializer.data)
