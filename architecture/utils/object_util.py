class ObjectUtil(object):

    @classmethod
    def is_not_none(cls, obj: any) -> any:
        return obj is not None

    @classmethod
    def is_none(cls, obj: any) -> any:
        return obj is None

    @classmethod
    def convert_json_to_object(cls, json: dict, obj: object):
        if cls.is_not_none(json) and cls.is_not_none(obj):
            for value in json:
                if hasattr(obj, value):
                    if type(json.get(value)) == list:
                        for i in json.get(value):
                            cls.convert_json_to_object(i, obj.__getattribute__(value))
                    else:
                        obj.__setattr__(value, json.get(value))

        return obj

    @classmethod
    def is_type(cls, value, _type):
        return type(value) == _type

    @classmethod
    def if_not_none(cls, condition, value_is_true, value_is_false):
        if cls.is_not_none(condition):
            return value_is_true
        else:
            return value_is_false
