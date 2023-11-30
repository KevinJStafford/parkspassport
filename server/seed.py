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
    Neighborhood.query.delete()
    Amenity.query.delete()
    Park.query.delete()

    print("Creating neighborhoods...")
    n1 = Neighborhood(name = "Park Slope")
    n2 = Neighborhood(name = "Bolivar")
    n3 = Neighborhood(name = "Brighton")
    n4 = Neighborhood(name = "Charles Town")
    n5 = Neighborhood(name = "Urbana")
    n6 = Neighborhood(name = "Bay Ridge")
    neighborhoods = [n1, n2, n3, n4, n5, n6]

    print("Creating amenities...")
    a1 = Amenity(amenity_items = "basketball court")
    a2 = Amenity(amenity_items = "dog park")
    a3 = Amenity(amenity_items = "hiking")
    a4 = Amenity(amenity_items = "campground")
    a5 = Amenity(amenity_items = "playground")
    a6 = Amenity(amenity_items = "bike trail")
    amenities = [a1, a2, a3, a4, a5, a6]

    print("Creating parks...")
    p1 = Park(name = "Jefferson County Memorial", location = "Charles Town, WV", neighborhood = n4, amenity = a1)
    p2 = Park(name = "Sam Michaels", location = "Harpers Ferry, WV", neighborhood = n2, amenity = a3)
    p3 = Park(name = "Caesar Creek State Park", location = "Waynesville, OH", neighborhood = n3, amenity = a4)
    p4 = Park(name = "Fido Field", location = "Cincinatti, OH", neighborhood = n5, amenity = a2)
    p5 = Park(name = "Slope Park Playground", location = "Brooklyn, NY", neighborhood = n1, amenity = a5)
    p6 = Park(name = "Owl's Head Park", location = "Brooklyn, NY", neighborhood = n6, amenity = a6)
    parks = [p1, p2, p3, p4, p5, p6]


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

