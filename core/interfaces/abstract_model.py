from architecture.utils.model_util import ModelUtil


class AbstractModel:
    def is_new(self):
        return ModelUtil.is_new(self)
