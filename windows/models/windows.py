from core.common.enums.enum_generic_status import EnumGenericStatus
from django.db import models


class Windows(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    path = models.CharField(max_length=255)
    version = models.CharField(max_length=8)
    upper = models.ForeignKey('self', on_delete=models.PROTECT, null=False)
    status = models.SmallIntegerField(choices=EnumGenericStatus.choices(), default=EnumGenericStatus.ENABLED)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'windows'
