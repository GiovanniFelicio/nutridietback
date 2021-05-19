from rest_framework import serializers
from architecture.utils.object_util import ObjectUtil
from architecture.exceptions.unprocessable import UnprocessableForm
from architecture.utils.string_util import StringUtil


class AbstractSerializer(serializers.Serializer):
    def to_model(self, cls):
        if not self.is_valid():
            raise UnprocessableForm()

        return cls(**self.data)
