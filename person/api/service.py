from person.models.person import Person
from person.api.serializer.person_serializer import PersonSerializer
from person.api.serializer.person_datatable_serializer import PersonDataTableSerializer
from architecture.utils.cpf_cnpj_util import CpfCnpjUtil
from architecture.utils.integer_util import IntegerUtil
from architecture.utils.date_util import DateUtil
from architecture.utils.datatable_util import DataTableUtil
from person.models.person_vo import PersonVO
from person.enum.enum_generic_status import EnumGenericStatus


class PersonService(object):

    def __init__(self):
        pass

    def create(self, model: Person):
        model.save()

    def validate_before_create(self, model: Person):
        is_valid_document: bool = CpfCnpjUtil.is_cpf_valid(model.document)
        is_valid_birth: bool = DateUtil.is_date_valid(model.date_birth)

        if not is_valid_document or not is_valid_birth:
            raise

    def resolve_person(self, serializer: PersonSerializer):
        model: Person = serializer.to_model(Person)
        model.document = IntegerUtil.only_numbers(model.document)
        self.validate_before_create(model)

        self.create(model)

    def resolve_data(self, request_data):
        persons = Person.manager.filter(status=EnumGenericStatus.ENABLED.value)

        return DataTableUtil.query_datatable(persons, PersonVO, PersonDataTableSerializer, request_data)
