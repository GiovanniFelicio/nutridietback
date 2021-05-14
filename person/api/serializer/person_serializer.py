from rest_framework import serializers
from core.interfaces import abstract_serializer
from person.api.serializer.person_email_serializer import PersonEmailSerializer
from core.enums.enum_generic_status import EnumGenericStatus
from person.api.serializer.person_phone_serializer import PersonPhoneSerializer
from person.enum.enum_document_type import EnumDocumentType
from person.enum.enum_gender_person import EnumGenderPerson


class PersonSerializer(abstract_serializer.AbstractSerializer):
    name = serializers.CharField(required=True)
    date_birth = serializers.DateField(required=True)
    document = serializers.CharField(required=True)
    document_type = serializers.ChoiceField(choices=EnumDocumentType.choices(), required=True)
    gender = serializers.ChoiceField(choices=EnumGenderPerson.choices())
    status = serializers.ChoiceField(choices=EnumGenericStatus.choices(), required=False)
    # person_emails = PersonEmailSerializer(many=True)
    # person_phones = PersonPhoneSerializer(many=True)
