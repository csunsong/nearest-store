import codecs
import csv

import utils


# Global Radius in miles and km
KM_RADIUS = 6367
MI_RADIUS = 3956


class CsvStoresIterator():

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with codecs.open(self.filename, 'rU', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            next(reader, None)
            for row in reader:
                yield row


class NearestObjectSearch():

    def __init__(self, units):
        self.units = units
        self.radius = KM_RADIUS if units == 'km' else MI_RADIUS

    def calc_distance(self, start_location, end_location):
        distance = utils.GeoDistancCalculator(
            self.radius).calc_distance(start_location, end_location)
        return distance

    def find_nearest(self, objects, coordinates):
        store_data = None
        closest_distance = self.radius
        for i in objects:
            current_distance = self.calc_distance(
                coordinates, (i['Latitude'], i['Longitude']))
            if current_distance < closest_distance:
                store_data = i
                store_data['Distance'] = current_distance
                store_data['Units'] = self.units
                closest_distance = current_distance
        return store_data
