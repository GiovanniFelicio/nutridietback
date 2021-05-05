from rest_framework import serializers
from core.interfaces import abstract_serializer
from person.api.serializer.person_email_serializer import PersonEmailSerializer
from core.enums.enum_generic_status import EnumGenericStatus
from person.enum.enum_genre_person import EnumGenrePerson


class PersonSerializer(abstract_serializer.AbstractSerializer):
    name = serializers.CharField(required=True)
    date_birth = serializers.DateField(required=True)
    document = serializers.CharField(required=True)
    genre = serializers.ChoiceField(choices=EnumGenrePerson.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())
    person_emails = PersonEmailSerializer(many=True)
