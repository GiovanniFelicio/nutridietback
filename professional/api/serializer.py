from rest_framework import serializers
from professional.models import Professional
from person.api.serializer.person_serializer import PersonSerializer


class ProfessionalSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Professional
        fields = '__all__'
