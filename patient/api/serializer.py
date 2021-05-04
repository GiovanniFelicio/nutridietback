from rest_framework import serializers
from patient.models import Patient
from person.api.serializer.person_serializer import PersonSerializer


class PatientSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Patient
        fields = '__all__'
