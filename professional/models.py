from django.db import models
from person.models.person import Person


class Professional(models.Model):
    person = models.ForeignKey(Person, null=False, on_delete=models.PROTECT)
    active = models.BooleanField(default=1)
    crn = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.person.name

    class Meta:
        db_table = 'professional'
