from architecture.utils.object_util import ObjectUtil


class ModelUtil:

    @staticmethod
    def is_new(model: object):
        if hasattr(model, 'id'):
            _id = model.__getattribute__('id')
            if ObjectUtil.is_type(_id, 'int'):
                return False

        return True