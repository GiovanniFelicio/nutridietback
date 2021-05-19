from core.common.interfaces.abstract_model import AbstractModel
from django.db import models
from person.api.manager import PersonManager
from person.models.person import Person
from core.common.enums.enum_generic_type import EnumGenericType
from core.common.enums.enum_generic_status import EnumGenericStatus


class PersonEmail(models.Model, AbstractModel):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='person_emails')
    email = models.EmailField()
    type = models.IntegerField(choices=EnumGenericType.choices())
    status = models.IntegerField(choices=EnumGenericStatus.choices(), default=EnumGenericStatus.ENABLED)

    manager = PersonManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'person_email'
