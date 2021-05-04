from patient.models import Patient


class PatientService(object):
    def __get_queryset(self):
        return Patient.manager

    def find_all(self, active):
        return self.__get_queryset().find_by_is_active(active)
