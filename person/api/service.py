from rest_framework.utils.serializer_helpers import ReturnDict

from architecture.exceptions.conflict import CustomConflict
from architecture.exceptions.enum_nd_exception_messages import EnumNDExceptionMessages
from architecture.exceptions.unprocessable import UnprocessableForm
from core.service.CrudService import CrudService
from person.models.person import Person
from person.api.serializer.person_serializer import PersonSerializer
from person.api.serializer.person_datatable_serializer import PersonDataTableSerializer
from architecture.utils.cpf_cnpj_util import CpfCnpjUtil
from architecture.utils.integer_util import IntegerUtil
from architecture.utils.date_util import DateUtil
from architecture.utils.datatable_util import DataTableUtil
from person.models.person_vo import PersonVO
from core.enums.enum_generic_status import EnumGenericStatus


class PersonService(CrudService):

    def __init__(self):
        super().__init__(Person)

    def validate_before_create_or_update(self, data: ReturnDict):
        is_valid_document: bool = CpfCnpjUtil.is_cpf_valid(data['document'])
        is_valid_birth: bool = DateUtil.is_date_valid(data['date_birth'])

        if not is_valid_document or not is_valid_birth:
            raise

    def resolve_person_for_create(self, serializer: PersonSerializer):
        data = self.resolve_person(serializer)

        person = Person.manager.find_by_document(document=data['document'])

        if person.exists():
            raise CustomConflict(EnumNDExceptionMessages.PERSON_DUPLICATE_INSERTED.value.format(data['document']))

        return self.create(**data)

    def resolve_person_for_update(self, pk: int, serializer: PersonSerializer):
        data = self.resolve_person(serializer)

        return self.update(pk, data)

    def resolve_person_for_delete(self, pk: int):

        return self.delete(pk)

    def resolve_person(self, serializer: PersonSerializer):
        if not serializer.is_valid():
            raise UnprocessableForm()

        data: ReturnDict = serializer.data
        data['document'] = IntegerUtil.only_numbers(data['document'])

        self.validate_before_create_or_update(data)

        return data

    def resolve_data(self, request_data):
        persons = Person.manager.filter(status=EnumGenericStatus.ENABLED.value)

        return DataTableUtil.query_datatable(persons, PersonVO, PersonDataTableSerializer, request_data)
