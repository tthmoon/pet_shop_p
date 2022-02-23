
class ApiAttributeError(AttributeError):
    def __init__(self, model_class, attr, value):
        complete_txt = "Model {} doesn't support this attribute {} {}".format(model_class, attr, type(value))
        super().__init__(complete_txt)
