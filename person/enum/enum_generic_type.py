from enum import IntEnum


class EnumGenericType(IntEnum):
    MAIN = 1
    WORK = 2
    COMMERCIAL = 3
    ADDITIONAL = 4

    @classmethod
    def choices(cls):
        return [(e.value, e.name) for e in cls]
