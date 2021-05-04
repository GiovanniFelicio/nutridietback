from rest_framework.decorators import action
from .serializer import PatientSerializer
from rest_framework.response import Response
from .service import PatientService
from core.interfaces.abstract_viewset import AbstractViewSet


class PatientViewSet(AbstractViewSet):
    patientService = PatientService()

    def list(self, request, *args, **kwargs):
        qs = self.patientService.find_all(True)
        serializer = PatientSerializer(qs, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return Response(self.get_status().HTTP_200_OK)
