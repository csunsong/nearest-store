"""
Find Store
  find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=(text|json)] [--csv=FILE]
  find_store --zip=<zip> 
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address=<address>  Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]
  --csv=FILE    	   Path to the csv file [default: store-locations.csv]


Example
  find_store --address="1770 Union St, San Francisco, CA 94123"
  find_store --zip=94115 --units=km
"""

from docopt import docopt
import find_store
import utils


def get_geocoder(options):
    if options['--address']:
        return utils.AddressGeocoder(options['--address'])
    return utils.ZipGeocoder(options['--zip'])


def get_formatter(options):
    if options.get('--output') == 'json':
        return utils.JsonStoreFormatter()
    return utils.TextStoreFormatter()


if __name__ == "__main__":
    options = docopt(__doc__)
    geocoder = get_geocoder(options)
    coordinates = geocoder.geocode()
    shops = find_store.CsvStoresIterator(options['--csv'])
    searcher = find_store.NearestObjectSearch(options['--units'])
    nearest = searcher.find_nearest(shops, coordinates)
    if nearest:
        formatter = get_formatter(options)
        print(formatter.format(nearest))
