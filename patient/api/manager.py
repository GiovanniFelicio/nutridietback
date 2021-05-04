from django.db.models import Manager
from architecture.utils.object_util import ObjectUtil


class PatientManager(Manager):
    def get_queryset(self):
        return super(PatientManager, self).get_queryset()

    def find(self, id: int):
        if ObjectUtil.is_not_none(id):
            return self.get_queryset().filter(id=id)

        return None

    def find_by_is_active(self, active: bool):
        if ObjectUtil.is_not_none(active):
            return self.get_queryset().filter(active=active)

        return None