from django.db import models
from person.enum.enum_generic_status import EnumGenericStatus


class PersonManager(models.Manager):
    def find_by_document(self, document: str):
        return self.filter(document=document)

    def find_by_status(self, status: EnumGenericStatus):
        return self.filter(status=status)
