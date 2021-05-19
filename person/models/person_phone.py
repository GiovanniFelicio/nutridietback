from core.common.interfaces.abstract_model import AbstractModel
from django.db import models
from person.api.manager import PersonManager
from person.models.person import Person
from core.common.enums.enum_generic_type import EnumGenericType
from core.common.enums.enum_generic_status import EnumGenericStatus


class PersonPhone(models.Model, AbstractModel):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='person_phones')
    phone = models.CharField(max_length=30)
    type = models.IntegerField(choices=EnumGenericType.choices(), default=EnumGenericType.MAIN)
    status = models.IntegerField(choices=EnumGenericStatus.choices(), default=EnumGenericStatus.ENABLED)

    manager = PersonManager()

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'person_phone'
