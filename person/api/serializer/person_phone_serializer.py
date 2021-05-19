from rest_framework import serializers
from core.common.interfaces import abstract_serializer
from core.common.enums.enum_generic_type import EnumGenericType
from core.common.enums.enum_generic_status import EnumGenericStatus


class PersonPhoneSerializer(abstract_serializer.AbstractSerializer):
    phone = serializers.CharField(max_length=30)
    type = serializers.ChoiceField(choices=EnumGenericType.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())