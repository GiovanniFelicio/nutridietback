from architecture.utils.model_util import ModelUtil


class AbstractModel:

    manager = None

    def is_new(self):
        return ModelUtil.is_new(self)
