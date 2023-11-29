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

class ParksInNeighborhood(Resource):
    def get(self):
        parks_in_neigborhood = [park.to_dict() for park in Park.query.all().neighborhood]
        return make_response(parks_in_neigborhood, 200)
    
api.add_resource(ParksInNeighborhood, '/neighborhoods/<int:id>/parks')
    
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

class ParkAmenities(Resource):
    def patch(self, id):
        park_amenity = Park.query.get(id).amenity_items
        if not park_amenity:
            return make_response({'error': 'Amenity not found!'}, 404)
        params = request.json
        try:
            for attr in params:
                setattr(park_amenity, attr, params[attr])
        except: 
            return make_response({'error': 'Try Again!'}, 422)
        db.session.commit()
        return make_response(park_amenity.to_dict(), 200)
    
api.add_resource(ParkAmenities, '/parks/<int:id>/amenities')

class ParksById(Resource):
    def delete(self, id):
        park = Park.query.get(id)
        if not park:
            return make_response({'error': 'Park not found!'}, 404)
        db.session.delete(park)
        db.session.commit()
        return make_response('', 204)
    
api.add_resource(ParksById, '/parks/<int:id>')

class Neighborhoods(Resource):
    def get(self):
        neighborhoods = [n.to_dict() for n in Neighborhood.query.all()]
        if not neighborhoods:
            return make_response({"Error" : "No neighborhoods found."}, 404)
        else:
            return make_response(neighborhoods, 200)
    def post(self):
        params = request.json
        try:
            new_neighborhood = Neighborhood(name = params["name"])
        except:
            return make_response({"Error": "Problem creating new neighborhood"}, 400)
        db.session.add(new_neighborhood)
        db.session.commit()
        return make_response(new_neighborhood.to_dict(), 201)
api.add_resource(Neighborhoods, "/neighborhoods")



class NeighborhoodById(Resource):
    def get(self, id):
        neighborhood_id = Neighborhood.query.get(id)
        if not neighborhood_id:
            return make_response({"Error" : "No neighborhoods with that id"}, 404)
        else:
            return make_response(neighborhood_id.to_dict(), 200)
    
    def delete(self, id):
        neighborhood_id = Neighborhood.query.get(id)
        if not neighborhood_id:
            return make_response({"Error": "No neighborhoods with that id"}, 404)
        db.session.delete(neighborhood_id)
        db.session.commit()
        return make_response("", 204)
api.add_resource(NeighborhoodById, "/neighborhoods/<int:id>")

class NeighborhoodAmenities(Resource):
    def get(self):
        neighborhood_amenities = [n.to_dict() for n in Neighborhood.query.all().amenities]
        return make_response(neighborhood_amenities, 200)
api.add_resource(NeighborhoodAmenities, "/neighborhoods/<int:id>/amenities")





@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

