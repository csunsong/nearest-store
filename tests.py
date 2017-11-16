import unittest
import find_store
import utils


class TestStoresIterator():

    def __init__(self):
        self.stores = [
            {'Store Name': 'San Francisco CBD East',
                'Latitude': 37.790841, 'Longitude': -122.4012802},
            {'Store Name': 'San Francisco South',
                'Latitude': 37.7252648, 'Longitude': -122.4615817},
            {'Store Name': 'San Mateo', 'Latitude': 37.5582963,
                'Longitude': -122.2835174}
        ]

    def __iter__(self):
        for store in self.stores:
            yield store


class TestGeoConversion(unittest.TestCase):

    def setUp(self):
        self.test_address = "1770 Union St, San Francisco, CA 94123"
        self.zip_code = "94123"

    def test_convert_address_to_coords(self):
        address_conv = utils.AddressGeocoder(self.test_address)
        coords = address_conv.geocode()
        self._test_coordinates_response(coords)

    def test_convert_zip_to_coords(self):
        zip_code_conv = utils.ZipGeocoder(self.zip_code)
        coords = zip_code_conv.geocode()
        self._test_coordinates_response(coords)

    def _test_coordinates_response(self, coords):
        self.assertIsInstance(coords, tuple)
        self.assertEqual(len(coords), 2)
        self.assertIsInstance(coords[0], float)
        self.assertIsInstance(coords[1], float)


class TestGeoDistancCalculator(unittest.TestCase):

    def setUp(self):
        self.mi_radius = find_store.MI_RADIUS
        self.km_radius = find_store.KM_RADIUS
        self.first_location = (37.3297085, -121.9031599)  # San Jose
        self.second_location = (37.5600336, -122.2688522)  # Foster City

    def test_calc_distance_miles(self):
        geo_calculator = utils.GeoDistancCalculator(
            self.first_location, self.second_location, self.mi_radius)
        distance = geo_calculator.calc_distance()
        self.assertAlmostEqual(distance, 25.588, places=3)

    def test_calc_distance_miles(self):
        geo_calculator = utils.GeoDistancCalculator(self.km_radius)
        distance = geo_calculator.calc_distance(
            self.first_location, self.second_location)
        self.assertAlmostEqual(distance, 41.183, places=3)


class TestNearestObjectSearchTest(unittest.TestCase):

    def setUp(self):
        self.search_coords = (37.7998285, -122.4141306)
        self.stores = TestStoresIterator()

    def test_find_nearest_in_miles(self):
        search = find_store.NearestObjectSearch('mi')
        nearest_store = search.find_nearest(self.stores, self.search_coords)
        self.assertAlmostEqual(nearest_store['Distance'], 0.936, places=3)
        self.assertEqual('San Francisco CBD East', nearest_store['Store Name'])

    def test_find_nearest_in_km(self):
        search = find_store.NearestObjectSearch('km')
        nearest_store = search.find_nearest(self.stores, self.search_coords)
        self.assertAlmostEqual(nearest_store['Distance'], 1.5069, places=3)
        self.assertEqual('San Francisco CBD East', nearest_store['Store Name'])


if __name__ == '__main__':
    unittest.main()
