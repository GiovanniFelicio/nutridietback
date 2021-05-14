from django.core.exceptions import ObjectDoesNotExist

from architecture.exceptions.badrequest import BadRequestCRUD


class CrudService(object):

    def __init__(self, model):
        self.model = model

    def create(self, **kwargs):
        _model = None

        try:
            _model = self.model.manager.create(**kwargs)
        except Exception as ex:
            raise BadRequestCRUD()

        return _model

    def update(self, pk: int, data):
        _model = None

        try:
            _model = self.model.manager.get(pk=pk)
            self.model.manager.update_or_create(pk=pk, defaults=data)
        except Exception as ex:
            raise BadRequestCRUD()

        return _model

    def delete(self, pk: int):
        try:
            _model = self.model.manager.get(pk=pk)
            _model.delete()
        except Exception as ex:
            raise BadRequestCRUD()

        return True