from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
from enums import GenreEnum, StateEnum
import re
from models import Venue, Artist, Show

def is_valid_phone(number):
    """ Validate phone numbers like:
    1234567890 - no space
    123.456.7890 - dot separator
    123-456-7890 - dash separator
    123 456 7890 - space separator
    """
    # Patterns:
    #000 = [[0-9]{3}
    #0000 = [0-9]{4}
    #-.  = ?[-. ]
    regex = re.compile('^\(?([0-9]{3}\)?[-. ]?([0-9]{3})[-. ]?(0-9]{4})$')
    return regex.match(number)

def is_valid_name(name):
    return name != None

def is_valid_city(city):
    return city != None

def is_valid_state(state):
    return state != None

def is_valid_address(address):
    return address != None 

def is_valid_image_link(image_link):
    valid_file_extensions = ['.webp', '.svg', '.png', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp']
    if len(image_link) < 1: return True
    for fe in valid_file_extensions:
        if fe in image_link: 
            return True
    return False

def is_valid_facebook_link(facebook_link):
    if len(facebook_link) < 1: return True
    if 'https://www.facebook.com/' not in facebook_link:
        return False
    return True

def is_valid_seeking_talent(seeking_talent):
    if not len(seeking_talent):
        return True
    else if seeking_talent == 'y':
        return True
    else return False

def is_valid_seeking_venue(seeking_venue):
    if not len(seeking_venue):
        return True
    else if seeking_venue == 'y':
        return True
    else return False

def is_valid_seeking_description(seeking_description):
    MAX_CHARACTERS = 500
    if len(seeking_description) > 0 and len(seeking_description) < MAX_CHARACTERS:
        return True
    else return False

def is_valid_start_time(start_time, venue_id, artist_id):
    try:
        artist_booked_times = Artist.query.filter_by(id=artist_id).filter_by(dates_booked)
        venue_booked_times =  Venue.query.filter_by(id=venue_id).filter_by(dates_booked)
        if start_time in artist_booked_times or start_time in venue_booked_times:
            return False
    except:
        #either artist or venue id not found
        return False
    if not len(start_time): 
        return False
    return True

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

    def validate(self):
        """ Custom validate method """
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_start_time(self.start_time):
            self.start_time.errors.append('Invalid start_time')
            return False

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices = StateEnum.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=GenreEnum.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )

    def validate(self):
        """ Custom validate method """
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Invalid phone.')
            return False
        if not is_valid_name(self.name.data):
            self.name.errors.append('Invalid name')
            return False
        if not is_valid_city(self.city.data):
            self.city.errors.append('Invalid city')
            return False
        if not is_valid_state(self.state.data):
            self.state.errors.append('Invalid state')
            return False
        if not is_valid_address(self.address.data):
            self.address.errors.append('Invalid address')
            return False
        if not is_valid_image_link(self.image_link.data):
            self.image_link.errors.append('Invalid image_link')
            return False
        if not is_valid_facebook_link(self.facebook_link.data):
            self.facebook_link.errors.append('Invalid facebook_link')
            return False
        if not is_valid_seeking_talent(self.seeking_talent.data):
            self.seeking_talent.errors.append('Invalid seeking_talent')
            return False
        if not is_valid_seeking_description(self.seeking_description.data):
            self.seeking_description.errors.append('Invalid seeking_description')
            return False
        #if pass validation
        return True



class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=StateEnum.choices()
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=GenreEnum.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

    def validate(self):
        """ Custom validate method """
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if not is_valid_phone(self.phone.data):
            self.phone.errors.append('Invalid phone.')
            return False
        if not is_valid_name(self.name.data):
            self.name.errors.append('Invalid name')
            return False
        if not is_valid_city(self.city.data):
            self.city.errors.append('Invalid city')
            return False
        if not is_valid_state(self.state.data):
            self.state.errors.append('Invalid state')
            return False
        if not is_valid_address(self.address.data):
            self.address.errors.append('Invalid address')
            return False
        if not is_valid_image_link(self.image_link.data):
            self.image_link.errors.append('Invalid image_link')
            return False
        if not is_valid_facebook_link(self.facebook_link.data):
            self.facebook_link.errors.append('Invalid facebook_link')
            return False
        if not is_valid_seeking_venue(self.seeking_venue.data):
            self.seeking_venue.errors.append('Invalid seeking_venue')
            return False
        if not is_valid_seeking_description(self.seeking_description.data):
            self.seeking_description.errors.append('Invalid seeking_description')
            return False
        if not is_valid_availability(self.availability.data):
            self.availability.errors.append('Invalid availability')
            return False
        #if pass validation
        return True

        #if pass validation
        return True
