from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = 'd25ac72e7a1e43b8a2d3c939895889d1'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(30.6652274, 76.88169309999999)
pprint(results)
# [{'components': {'city': 'Bordeaux',
#                  'country': 'France',
#                  'country_code': 'fr',
#                  'county': 'Bordeaux',
#                  'house_number': '11',
#                  'political_union': 'European Union',
#                  'postcode': '33800',
#                  'road': 'Rue Sauteyron',
#                  'state': 'New Aquitaine',
#                  'suburb': 'Bordeaux Sud'},
#   'formatted': '11 Rue Sauteyron, 33800 Bordeaux, France',
#   'geometry': {'lat': 44.8303087, 'lng': -0.5761911}}]