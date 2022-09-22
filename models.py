#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Enum
from enums import *

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask('app')
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

shows = db.Table('Show',
    db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
    db.Column('start_time', db.DateTime(timezone=False))
)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    #genres = db.Column('genres', Enum(GenreEnum)) 
    genres = db.Column(db.String(120)) 
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    date_listed = db.Column(db.TIMESTAMP(timezone=False), server_default=func.now())

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone 

    def set_image_link(self, image_link):
        self.image_link = image_link 

    def set_facebook_link(self, facebook_link):
        self.facebook_link = facebook_link 

    def set_genres(self, genres):
        self.genres = genres

    def set_website_link(self, website_link):
        self.website_link = website_link 

    def set_seeking_talent(self, seeking_talent):
        self.seeking_talent = seeking_talent 

    def set_seeking_description(self, seeking_description):
        self.seeking_description = seeking_description 

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def view(self):
      print("name" + ": " +  self.name)
      print("city" + ": " +  self.city)
      print("state" + ": " +  self.state)
      print("address" + ": " +  self.address)
      print("phone" + ": " +  self.phone)
      print("image" + ": " +  self.image_link)
      print("facebook" + ": " +  self.facebook_link)
      print("genres" + ": " +  self.genres,)
      print("website" + ": " +  self.website_link)
      print("seeking_talent" + ": " +  self.seeking_talent)
      print("seeking_description" + ": " +  self.seeking_description)
      print("date_listed" + ": " +  self.date_liste)
      return None

    #def format(self):
    #    return {
    #        "id": self.id,
    #        "name": self.name,
    #        "city": self.city,
    #        "state": self.self.state,
    #        "address": self.address,
    #        "phone": self.phone,
    #        "image": self.image_link,
    #        "facebook": self.facebook_link,
    #        "genres": self.genres, 
    #        "website": self.website_link,
    #        "seeking_talent": self.seeking_talent,
    #        "seeking_description": self.seeking_description,
    #        "date_listed": self.date_listed
    #    }


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    #genres = db.Column('genres', Enum(GenreEnum)) 
    genres = db.Column(db.String(120)) 
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column('value', Enum(GenreEnum)) 
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    date_listed = db.Column(db.TIMESTAMP(timezone=False), server_default=func.now())
    availability = db.Column(db.String(500))

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_phone(self, phone):
        self.phone = phone 

    def set_image_link(self, image_link):
        self.image_link = image_link 

    def set_facebook_link(self, facebook_link):
        self.facebook_link = facebook_link 

    def set_genres(self, genres):
        self.genres = genres

    def set_website_link(self, website_link):
        self.website_link = website_link 

    def set_seeking_venue(self, seeking_venue):
        self.seeking_venue = seeking_venue 

    def set_seeking_description(self, seeking_description):
        self.seeking_description = seeking_description 

    def set_availability(self, availability):
        self.availability = availability 

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def view(self):
        print("id" + ": " + self.id)
        print("name" + ": " +  self.name)
        print("city" + ": " +  self.city)
        print("state" + ": " +  self.state)
        print("address" + ": " +  self.address)
        print("phone" + ": " +  self.phone)
        print("image" + ": " +  self.image_link)
        print("facebook" + ": " +  self.facebook_link)
        print("genres" + ": " +  self.genres,)
        print("website" + ": " +  self.website_link)
        print("seeking_talent" + ": " +  self.seeking_talent)
        print("seeking_description" + ": " +  self.seeking_description)
        print("date_listed" + ": " +  self.date_liste)

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "state": self.self.state,
            "address": self.address,
            "phone": self.phone,
            "image": self.image_link,
            "facebook": self.facebook_link,
            "genres": self.genres, 
            "website": self.website_link,
            "seeking_venue": self.seeking_venue,
            "seeking_description": self.seeking_description,
            "date_listed": self.date_listed,
            "availability": self.availability
        }
