from rest_framework import serializers
from core.interfaces import abstract_serializer
from core.enums.enum_generic_type import EnumGenericType
from core.enums.enum_generic_status import EnumGenericStatus


class PersonPhoneSerializer(abstract_serializer.AbstractSerializer):
    phone = serializers.CharField(max_length=30)
    type = serializers.ChoiceField(choices=EnumGenericType.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())