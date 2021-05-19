from rest_framework import serializers
from core.common.interfaces import abstract_serializer
from core.common.enums.enum_generic_type import EnumGenericType
from core.common.enums.enum_generic_status import EnumGenericStatus


class PersonEmailSerializer(abstract_serializer.AbstractSerializer):
    email = serializers.EmailField()
    type = serializers.ChoiceField(choices=EnumGenericType.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices())
