from rest_framework.viewsets import ViewSet
from .serializer.person_serializer import PersonSerializer
from person.models.person import Person
from rest_framework.response import Response
from rest_framework import status
from person.api.service import PersonService
from core.enums.enum_generic_status import EnumGenericStatus
from rest_framework.decorators import action



class PersonViewSet(ViewSet):
    personService = PersonService()

    def list(self, request, *args, **kwargs) -> Response:
        serializer = PersonSerializer(Person.manager.find_by_status(EnumGenericStatus.ENABLED), many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        ds = PersonSerializer(data=request.data)

        self.personService.resolve_person(ds)

        return Response(status.HTTP_200_OK)

    @action(methods=['post'], url_path='data', detail=False)
    def data(self, request, *args, **kwargs):
        data = self.personService.resolve_data(request.data)

        return Response(data)