from core.interfaces.abstract_vo import AbstractVO


class PersonVO:
    NAME = AbstractVO('name', 'Name')
    DATE_BIRTH = AbstractVO('date_birth', 'Birth')
    DOCUMENT = AbstractVO('document', 'Document')
    GENRE = AbstractVO('genre', 'Genre')
    STATUS = AbstractVO('status', 'Status')

    values = [NAME, DATE_BIRTH,DOCUMENT, GENRE, STATUS]

    @classmethod
    def get_values(cls):
        return cls.values
