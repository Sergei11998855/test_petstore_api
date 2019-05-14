from jsonmodels import models
from jsonmodels.fields import ListField, EmbeddedField, IntField, StringField


class Category(models.Base):
    id = IntField()
    name = StringField()


class Tag(models.Base):
    id = IntField()
    name = StringField()


class Pet(models.Base):
    id = IntField()
    category = EmbeddedField(Category)
    name = StringField()
    photo_urls = ListField(str)
    tags = ListField(Tag)
    status = StringField()

