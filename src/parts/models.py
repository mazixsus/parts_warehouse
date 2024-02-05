from mongoengine import Document, EmbeddedDocument, fields
from categories.models import Category

LOCATION_OPTION = [
    ("room", "Room"),
    ("bookcase", "Bookcase"),
    ("shelf", "Self"),
    ("cuvette", "Cuvette"),
    ("column", "Column"),
    ("row", "Row"),
]

class Parts(Document):
    serial_number = fields.StringField(required=True, reqmax_length=20, unique=True)
    name = fields.StringField(required=True, max_length=20, unique=True)
    description = fields.StringField(required=True, max_length=255)
    category = fields.StringField(required=True)
    category_reference = fields.ReferenceField(Category, required=True)
    quantity = fields.IntField(required=True)
    price= fields.DecimalField(required=True, decimal_places=2)
    location_option = fields.ListField(field=fields.StringField(choices=LOCATION_OPTION), required=True)