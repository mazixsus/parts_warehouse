from mongoengine import Document, EmbeddedDocument, fields
from bson.objectid import ObjectId

class Category(Document):
    name = fields.StringField(required=True, primary_key=True)
    parent = fields.ReferenceField("self", null=True)