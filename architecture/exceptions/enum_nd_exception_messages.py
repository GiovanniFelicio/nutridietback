from enum import Enum


class EnumNDExceptionMessages(Enum):
    PERSON_DUPLICATE_INSERTED = 'Não foi possível inserir, pois já existe uma pessoa com o documento: {}'
