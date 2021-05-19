from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from architecture.exceptions.enum_nd_exception_messages import EnumNDExceptionMessages
from person.api.serializer.person_address_serializer import PersonAddressSerializer
from person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    person_address = PersonAddressSerializer()
    document = serializers.CharField(
        validators=[UniqueValidator(queryset=Person.objects.all(), message=EnumNDExceptionMessages.PERSON_DUPLICATE_INSERTED.value)])

    class Meta:
        model = Person
        fields = ('name', 'date_birth', 'document', 'document_type', 'gender', 'status', 'person_address')
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Nome'),
                    'blank': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Nome')
                }
            },
            'date_birth': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Data de Nascimento'),
                    'blank': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Data de Nascimento')
                }
            },
            'document': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Documento'),
                    'blank': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Documento')
                }
            },
            'document_type': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Tipo de Documento'),
                    'blank': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Tipo de Documento')
                }
            },
            'gender': {
                'error_messages': {
                    'required': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Gênero'),
                    'blank': EnumNDExceptionMessages.REQUIRED_FIELD.value.format('Gênero')
                }
            }
        }

    @transaction.atomic()
    def create(self, validated_data):
        person_address_data = validated_data.pop('person_address')

        person = Person.objects.create(**validated_data)

        person_address_data['person'] = person
        person_address_serializer = PersonAddressSerializer(data=person_address_data)
        person_address_serializer.is_valid(raise_exception=True)
        person_address = person_address_serializer.create(person_address_data)

        return person

