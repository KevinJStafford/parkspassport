from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Neighborhood(db.Model, SerializerMixin):
    __tablename__ = "neighborhoods"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)


