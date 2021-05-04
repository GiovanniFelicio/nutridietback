from person.models.person import Person
from architecture.validators.validator_required_fields import ValidatorRequiredFields


class PersonValidator:

    def __init__(self):
        pass

    def validate_required_fields_create(self, model: Person) -> bool:
        validator: ValidatorRequiredFields = ValidatorRequiredFields()
        validator.add('name', model.name)
        validator.add('date_birth', model.date_birth)
        validator.add('document', model.document)
        return validator.validate()
