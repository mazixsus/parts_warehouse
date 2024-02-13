from mongoengine import Document, EmbeddedDocument, fields
from bson.objectid import ObjectId

class Category(Document):
    name = fields.StringField(required=True, unique=True, primary_key=True)
    # parent_name = fields.StringField(required=False, null=True, default=None, unique=False)
    parent = fields.ReferenceField("self", null=True)
    # display_name = fields.StringField(required=True, max_length=30)
    # parents_tree = fields.ListField(field=fields.StringField(max_length=30))