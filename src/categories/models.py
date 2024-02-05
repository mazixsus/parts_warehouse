from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.
class Category(Document):
    #id = fields.StringField(required=True, primary_key=True)
    name = fields.StringField(required=True, unique=True)
    parent_name = fields.StringField(null=True, default=None)
    parent = fields.ReferenceField('self', required=False, null=True, default=None)