from django.db import models

from person.api.managers import PersonAddressManager
from person.models import Person


class PersonAddress(models.Model):

    code = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField()
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=4)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person_address')

    objects = PersonAddressManager()

    class Meta:
        db_table = 'person_address'
