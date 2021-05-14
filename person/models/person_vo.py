from core.interfaces.abstract_vo import AbstractVO


class PersonVO:
    NAME = AbstractVO('name', 'Name')
    DATE_BIRTH = AbstractVO('date_birth', 'Birth')
    DOCUMENT = AbstractVO('document', 'Document')
    GENDER = AbstractVO('gender', 'Gender')
    STATUS = AbstractVO('status', 'Status')

    values = [NAME, DATE_BIRTH, DOCUMENT, GENDER, STATUS]

    @classmethod
    def get_values(cls):
        return cls.values
