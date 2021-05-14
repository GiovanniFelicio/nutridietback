from enum import Enum


class EnumDocumentType(Enum):
    CPF = 'CPF'
    CNPJ = 'CNPJ'
    RG = 'RG'

    @classmethod
    def choices(cls):
        return [(e.value, e.name) for e in cls]
