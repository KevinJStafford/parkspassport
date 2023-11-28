from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db


class Park(db.Model, SerializerMixin):
    __tablename__ = 'parks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    amenities = db.relationship('Amenity', back_populates = 'park', cascade = 'all, delete-orphan')
    neighborhoods = association_proxy('amenities', 'neighborhood')

    serialize_rules = ('-amenities.park', )

    @validates('name')
    def check_name(self, key, new_name):
        if len(new_name) < 3:
            raise ValueError('Name must be longer than 3 characters!')
        return new_name
    
    @validates('location')
    def check_location(self, key, new_location):
        if len(new_location) < 3:
            raise ValueError('Location must be longer than 3 characters!')
        return new_location

    def __repr__(self):
        return f'<Park {self.name}>'

class Neighborhood(db.Model, SerializerMixin):
    __tablename__ = "neighborhoods"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    amenities = db.relationship('Amenity', back_populates = 'neighborhood', cascade = 'all, delete-orphan')
    parks = association_proxy('amenities', 'park')

    serialize_rules = ('-amenities.neighborhood', )

    @validates('name')
    def check_name(self, key, new_name):
        if len(new_name) < 3:
            raise ValueError('Name must be longer than 3 characters!')
        return new_name

    def __repr__(self):
        return f'<Neighborhood {self.name}>'

class Amenity(db.Model, SerializerMixin):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key = True)
    amenity_items = db.Column(db.String)

    park_id = db.Column(db.ForeignKey('parks.id'))
    neighborhood_id = db.Column(db.ForeignKey('neighborhoods.id'))

    park = db.relationship('Park', back_populates = 'amenities')
    neighborhood = db.relationship('Neighborhood', back_populates = 'amenities')

    @validates('amenity_items')
    def check_amenity_items(self, key, new_amenity_items):
        if len(new_amenity_items) < 3:
            raise ValueError('Amenity must be longer than 3 characters!')
        return new_amenity_items

    def __repr__(self):
        return f'<Amenity {self.amenity_list}>'
    