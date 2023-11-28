#!/usr/bin/env python3

# Standard library imports
from random import choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Park, Neighborhood, Amenity


with app.app_context():
    print("Deleting data...")
    Park.query.delete()
    Neighborhood.query.delete()

    print("Creating parks...")
    p1 = Park(name = "Jefferson County Memorial", location = "Charles Town, WV")
    p2 = Park(name = "Sam Michaels", location = "Harpers Ferry, WV")
    p3 = Park(name = "Caesar Creek State Park", location = "Waynesville, OH")
    p4 = Park(name = "Fido Field", location = "Cincinatti, OH")
    p5 = Park(name = "Slope Park Playground", location = "Brooklyn, NY")
    p6 = Park(name = "Owl's Head Park", location = "Brooklyn, NY")
    parks = [p1, p2, p3, p4, p5, p6]


    print("Creating neighborhoods...")
    n1 = Neighborhood(name = "Park Slope")
    n2 = Neighborhood(name = "Bolivar")
    n3 = Neighborhood(name = "Brighton")
    n4 = Neighborhood(name = "Charles Town")
    n5 = Neighborhood(name = "Urbana")
    n6 = Neighborhood(name = "Bay Ridge")
    neighborhoods = [n1, n2, n3, n4, n5, n6]


    print("Creating amenities...")
    a1 = Amenity(amenity_items = "basketball court", park = p1, neighborhood = n4)
    a2 = Amenity(amenity_items = "dog park", park = p4, neighborhood = n5)
    a3 = Amenity(amenity_items = "hiking", park = p2, neighborhood = n2)
    a4 = Amenity(amenity_items = "campground", park = p3, neighborhood = n3)
    a5 = Amenity(amenity_items = "playground", park = p5, neighborhood = n1)
    a6 = Amenity(amenity_items = "bike trail", park = p6, neighborhood = n6)
    amenities = [a1, a2, a3, a4, a5, a6]


    db.session.add_all(parks)
    db.session.add_all(neighborhoods)
    db.session.add_all(amenities)
    db.session.commit()



# FAKER SEED DATA BELOW!
# fake = Faker()   
# def create_parks():
#     parks = []
#     for _ in range(10):
#         p = Park(
#             name=fake.name(),
#             location=fake.name(),
#             )
#         parks.append(p)
#     return parks
        
# def create_neighborhoods():
#     neighborhoods = []
#     for _ in range(10):
#         n = Neighborhood(
#             name=fake.name()
#         )
#         neighborhoods.append(n)
#     return neighborhoods
        
# if __name__ == '__main__':
     
#      with app.app_context():
#         print("Clearing db...")
#         Park.query.delete()
#         Neighborhood.query.delete()

#         print("Seeding parks...")
#         parks = create_parks()
#         db.session.add_all(parks)
#         db.session.commit()

#         print("Seeding neighborhoods...")
#         neighborhoods = create_neighborhoods()
#         db.session.add_all(neighborhoods)
#         db.session.commit()

#         print("Done seeding")

