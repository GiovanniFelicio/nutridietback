from core.interfaces.abstract_model import AbstractModel
from django.db import models
from person.api.manager import PersonManager
from person.enum.enum_genre_person import EnumGenrePerson
from core.enums.enum_generic_status import EnumGenericStatus
from architecture.utils.object_util import ObjectUtil


class Person(models.Model, AbstractModel):
    name = models.CharField(max_length=100, null=False)
    date_birth = models.DateField()
    document = models.CharField(max_length=14, unique=True)
    genre = models.CharField(choices=EnumGenrePerson.choices(), max_length=6)
    status = models.SmallIntegerField(choices=EnumGenericStatus.choices(), default=EnumGenericStatus.ENABLED)

    manager = PersonManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(args) == 1:
            for p in args:
                ObjectUtil.convert_json_to_object(p, self)

        print(self)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
