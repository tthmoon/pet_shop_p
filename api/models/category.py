from api.models.base_model import BaseModel


class Category(BaseModel):

    attribute_type_map = {
        'name': str,
        'id': int,
    }
