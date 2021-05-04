from django.db import models
from person.models.person import Person
from patient.api.manager import PatientManager


class Patient(models.Model):
    person = models.ForeignKey(Person, null=False, on_delete=models.PROTECT)
    active = models.BooleanField(default=1)

    manager = PatientManager()

    def __str__(self):
        return self.person.name

    class Meta:
        db_table = 'patient'
