from rest_framework import serializers
from architecture.exceptions.enum_nd_exception_messages import EnumNDExceptionMessages
from person.models import PersonAddress


class PersonAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAddress
        fields = ('code', 'address', 'complement', 'number', 'district', 'city', 'state')
        extra_kwargs = {
            'code': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('CEP')
                }
            },
            'address': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Logradouro')
                }
            },
            'number': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Número')
                }
            },
            'district': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Bairro')
                }
            },
            'city': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Cidade')
                }
            },
            'state': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Estado')
                }
            }
        }

    def create(self, validated_data):
        return PersonAddress.objects.create(**validated_data)
