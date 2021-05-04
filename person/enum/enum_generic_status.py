from enum import IntEnum


class EnumGenericStatus(IntEnum):
    ENABLED = 1
    DISABLED = 0

    @classmethod
    def choices(cls):
        return [(e.value, e.name) for e in cls]
