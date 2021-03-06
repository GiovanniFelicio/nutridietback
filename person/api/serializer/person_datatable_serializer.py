from rest_framework import serializers
from core.common.interfaces import abstract_serializer
from core.common.enums.enum_generic_status import EnumGenericStatus
from person.enum.enum_gender_person import EnumGenderPerson


class PersonDataTableSerializer(abstract_serializer.AbstractSerializer):
    name = serializers.CharField(required=True)
    date_birth = serializers.DateField(required=True)
    document = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=EnumGenderPerson.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())
