from api.models.base_model import BaseModel


class Tag(BaseModel):

    attribute_type_map = {
        'name': str,
        'id': int,
    }
