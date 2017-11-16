import json
import math
import zipcode
from geopy.geocoders import Nominatim


class ZipGeocoder():

    def __init__(self, input_zip):
        self.input_zip = input_zip

    def geocode(self):
        location = zipcode.isequal(self.input_zip)
        return location.lat, location.lon


class AddressGeocoder():

    def __init__(self, input_address):
        self.input_address = input_address

    def geocode(self):
        location = Nominatim().geocode(self.input_address)
        return location.latitude, location.longitude


class GeoDistancCalculator():

    def __init__(self, radius):
        self.radius = radius

    def calc_distance(self, start_location, end_location):
        lat1, lon1 = (float(v) for v in start_location)
        lat2, lon2 = (float(v) for v in end_location)
        radius = self.radius
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c
        return distance


class TextStoreFormatter():

    def format(self, response):
        response = "Closest store is {Store Name}, located at {Store Location},"\
            " {Address}, {City}, {State} in {Zip Code}, {County} {Distance}"\
            " {Units} away".format(**response)
        return response


class JsonStoreFormatter():

    def format(self, response):
        return json.dumps(response)
