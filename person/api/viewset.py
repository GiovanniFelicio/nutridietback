from rest_framework.viewsets import ViewSet

from architecture.exceptions.unprocessable import CustomUnprocessable
from core.enums.enum_messages_validate import EnumMessagesValidate
from .serializer.person_serializer import PersonSerializer
from person.models.person import Person
from rest_framework.response import Response
from rest_framework import status
from person.api.service import PersonService
from core.enums.enum_generic_status import EnumGenericStatus
from rest_framework.decorators import action


class PersonViewSet(ViewSet):
    personService = PersonService()

    def retrieve(self, request, pk=None):
        person: Person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)

        return Response(serializer.data)

    def list(self, request, *args, **kwargs) -> Response:
        serializer = PersonSerializer(Person.manager.find_by_status(EnumGenericStatus.ENABLED), many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        ds = PersonSerializer(data=request.data)

        person = self.personService.create_person(ds)

        return Response({'id': person.id, 'message': 'Criado com Sucesso !!'}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs) -> Response:
        ds = PersonSerializer(data=request.data)

        pk = kwargs.get('pk')

        if pk is None:
            raise CustomUnprocessable("Código de pessoa inválido !")

        person = self.personService.resolve_person_for_update(pk, ds)

        return Response({'id': person.id, 'message': 'Atualizado com Sucesso !!'}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        pass

    @action(methods=['post'], url_path='data', detail=False)
    def data(self, request, *args, **kwargs):
        data = self.personService.resolve_data(request.data)

        return Response(data)
