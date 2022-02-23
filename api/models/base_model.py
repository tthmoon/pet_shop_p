import json
from api.custom_errors_exceptions.exceptions import ApiAttributeError

class BaseModel:
    attribute_type_map = {}

    ## Вызов конструктора с полями, которые не описаны в attribute_type_map должен вызывать ошибку
    ## Чтение и запись полей может выполняться с любыми данными и полями
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if not self.is_attr_in_attr_map(name, value):
                raise ApiAttributeError(self.__class__, name, value)
            setattr(self, name, value)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __getitem__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]

    def __contains__(self, name):
        return name in self.__dict__[name]

    def __eq__(self, another):
        ## нужен механизм устнановки игнорируемых полей, либо использование готового решения6 которое поддерживает это
        if not isinstance(another, self.__class__):
            return False
        if not set(self.__dict__.keys()) == set(another.__dict__.keys()):
            return False
        for _var, _val in self.__dict__.items():
            if _val != another.__dict__[_var]:
                return False
        return True

    def is_attr_in_attr_map(self, attr, value):
        return attr in self.attribute_type_map.keys() and type(value) == self.attribute_type_map[attr]

    @classmethod
    def from_json(cls, json_str):
        return json.loads(json_str, object_hook=lambda d: cls(**d))
