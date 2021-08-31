import populartimes
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='')

# Geocoding an address
place_id_restaurant = gmaps.places(query = 'Restaurante',location = 'Zona T',radius = 500, language = 'spanish')
#restaurant_details = gmaps.places(place_id = place_id_restaurant['candidates'][0]['place_id'])

places = []

for restaurant in place_id_restaurant['results']:
    places.append(restaurant['place_id'])


api_key = ""
restaurants_popular_times = []


for place_id in places:
    restaurants_popular_times.append(populartimes.get_id(api_key,place_id))


for restaurant in restaurants_popular_times:
    print(restaurant['name'])
    print(restaurant['populartimes'])