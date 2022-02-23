from api.models.base_model import BaseModel
from api.models.category import Category

class Pet(BaseModel):

    attribute_type_map = {
        'name': str,
        'photoUrls': list,
        'id': int,
        'category': Category,
        'tags': list,
        'status': str,
    }
