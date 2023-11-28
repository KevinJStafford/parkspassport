#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from models import Neighborhood

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Neighborhood

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        

        Neighborhood.query.delete()

        n1 = Neighborhood(name="Fairfax Crossing")
        n2 = Neighborhood(name="Park Slope")
        n3 = Neighborhood(name = "Hyde Park")
