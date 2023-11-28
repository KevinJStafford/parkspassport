#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from models import Park, Amenity, Neighborhood
from flask_migrate import Migrate
from flask import Flask,request, make_response
from flask_restful import Resource, Api
import os

# Local imports
from config import app, db, api
# Add your model imports


class Parks(Resource):
    def get(self):
        parks = [park.to_dict() for park in Park.query.all()]
        return make_response(parks, 200)
    
    def post(self):
        params = request.json
        try:
            park = Park(name = params['name'], location = params['location'])
        except:
            return make_response({'errors': 'Try Again'}, 422)
        db.session.add(park)
        db.session.commit()
        return make_response(park.to_dict(), 201)

api.add_resource(Parks, '/parks')

class AmenitiesById(Resource):
    def patch(self, id):
        amenity = Amenity.query.get(id)
        if not amenity:
            return make_response({'error': 'Amenity not found!'}, 404)
        params = request.json
        try:
            for attr in params:
                





@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

