from rest_framework import serializers
from core.interfaces import abstract_serializer
from person.enum.enum_generic_type import EnumGenericType
from person.enum.enum_generic_status import EnumGenericStatus


class PersonEmailSerializer(abstract_serializer.AbstractSerializer):
    email = serializers.EmailField()
    type = serializers.ChoiceField(choices=EnumGenericType.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())
