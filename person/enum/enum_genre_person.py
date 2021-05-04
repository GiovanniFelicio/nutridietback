from enum import Enum


class EnumGenrePerson(Enum):
    MALE = 'M'
    FEMALE = 'F'

    @classmethod
    def choices(cls):
        return [(e.value, e.name) for e in cls]
