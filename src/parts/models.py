from mongoengine import Document, EmbeddedDocument, fields
from categories.models import Category

class Location(EmbeddedDocument):
    room = fields.StringField(max_length=30, required=True)
    bookcase = fields.StringField(max_length=30)
    shelf = fields.StringField(max_length=10)
    cuvette = fields.StringField(max_length=10)
    column = fields.StringField(max_length=10)
    row = fields.StringField(max_length=10)

class Parts(Document):
    serial_number = fields.StringField(required=True, primary_key=True, max_length=20)
    name = fields.StringField(required=True, max_length=20)
    description = fields.StringField(required=True, max_length=255)
    category = fields.ReferenceField(Category, required=True)
    quantity = fields.IntField(required=True)
    price= fields.DecimalField(required=True, decimal_places=2)
    location_option = fields.EmbeddedDocumentField(Location, required=True)