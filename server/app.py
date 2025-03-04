#!/usr/bin/env python3

# Remote library imports
from models import Park, Amenity, Neighborhood
from flask_migrate import Migrate
from flask import Flask,request, make_response
from flask_restful import Resource, Api
import os

# Local imports
from config import app, db, api
# There are a few routes that are not used in MVP that we plan to use for future enhancements. Marking those with a comment called "Not in MVP"

# Not used in MVP
class ParksInNeighborhood(Resource):
    def get(self, id):
        neighborhood_id = Neighborhood.query.get(id)
        if not neighborhood_id:
            return make_response({"Error": "No neighborhoods with that id."}, 404)
        parks_in_neighborhood = neighborhood_id.parks
        parks_data = [park.to_dict() for park in parks_in_neighborhood]
        return make_response(parks_data, 200)
    
api.add_resource(ParksInNeighborhood, '/neighborhoods/<int:id>/parks')


class Parks(Resource):
    def get(self):
        parks = [park.to_dict() for park in Park.query.all()]
        return make_response(parks, 200)

 # Not used in MVP   
    def post(self):
        params = request.json
        try:
            park = Park(name = params['name'], location = params['location'], neighborhood_id = params["neighborhood_id"], amenity_id = params["amenity_id"])
        except:
            return make_response({'errors': 'Try Again'}, 422)
        db.session.add(park)
        db.session.commit()
        return make_response(park.to_dict(), 201)

api.add_resource(Parks, '/parks')

# Not used in MVP
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

# Not used in MVP
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
        
 # Not used in MVP    
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

# Not used in MVP
class NeighborhoodById(Resource):
    def get(self, id):
        neighborhood_id = Neighborhood.query.get(id)
        if not neighborhood_id:
            return make_response({"Error" : "No neighborhoods with that id"}, 404)
        else:
            return make_response(neighborhood_id.to_dict(), 200)
# Not used in MVP    
    def delete(self, id):
        neighborhood_id = Neighborhood.query.get(id)
        if not neighborhood_id:
            return make_response({"Error": "No neighborhoods with that id"}, 404)
        db.session.delete(neighborhood_id)
        db.session.commit()
        return make_response("", 204)
api.add_resource(NeighborhoodById, "/neighborhoods/<int:id>")

# Not used in MVP
class NeighborhoodAmenities(Resource):
    def get(self):
        neighborhood_amenities = [n.to_dict() for n in Neighborhood.query.all().amenities]
        return make_response(neighborhood_amenities, 200)
api.add_resource(NeighborhoodAmenities, "/neighborhoods/<int:id>/amenities")


class Amenities(Resource):
    def get(self):
        amenities=[a.to_dict() for a in Amenity.query.all()]
        return make_response(amenities, 200)
    def post(self):
        params = request.json
        try:
            new_amenity = Amenity(amenity_items = params["amenityname"])
        except:
            return make_response({"Error" : "Try again"}, 422)
        db.session.add(new_amenity)
        db.session.commit()
        return make_response(new_amenity.to_dict(), 201)
api.add_resource(Amenities, '/amenities')

class AmenityById(Resource):
    def delete(self, id):
        amenity_id = Amenity.query.get(id)
        if not amenity_id:
            return make_response({"Error" : "no amenity found with that id"}, 404)
        db.session.delete(amenity_id)
        db.session.commit()
        return make_response("", 204)
    
    def patch(self,id):
        amenity = Amenity.query.get(id)
        if not amenity:
            return make_response({"Error" : "no amenity found with that id"}, 404)
        params = request.json
        for attr in params:
            setattr(amenity, attr, params[attr])
        db.session.commit()
        return make_response(amenity.to_dict(), 200)

api.add_resource(AmenityById, "/amenities/<int:id>")


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

