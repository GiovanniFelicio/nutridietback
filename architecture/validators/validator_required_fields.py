from architecture.utils.object_util import ObjectUtil


class ValidatorRequiredFields:
    def __init__(self):
        self.fields: list[dict] = []

    def validate(self):
        for field in self.fields:
            for key in field:
                if not ObjectUtil.is_not_none(field.get(key)):
                    raise Exception("Error de validação")

        return True

    def add(self, key: str, value: str):
        field = {key: value}
        self.fields.append(field)
        return self
