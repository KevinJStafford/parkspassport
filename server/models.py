from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db


class Park(db.Model, SerializerMixin):
    __tablename__ = 'parks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    amenities = db.relationship('Amenity', back_populates = 'amenities', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f'<Park {self.name}>'
    
class Amenity(db.Model, SerializerMixin):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key = True)
    amenity_list = db.Column(db.String)

    park_id = db.Column(db.ForeignKey('parks.id'))
    neighborhood_id = db.Column(db.ForeignKey('neighborhoods.id'))

    park = db.relationship('Park', back_populates = 'amenities')
    