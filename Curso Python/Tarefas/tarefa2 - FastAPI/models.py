
from mongoengine import Document, StringField, IntField, ListField, FloatField


class Product(Document):
    prod_id = IntField()
    name = StringField(max_length=100)
    price = FloatField()
    description = StringField()


class User(Document):
    username = StringField()
    password = StringField()


    

