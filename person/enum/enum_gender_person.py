from enum import Enum


class EnumGenderPerson(Enum):
    MALE = 'M'
    FEMALE = 'F'

    @classmethod
    def choices(cls):
        return [(e.value, e.name) for e in cls]
