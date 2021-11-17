import os
import time
import folium
import phonenumbers
from tqdm import std, tqdm
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# input number 

number = str(input("Enter a phone number: "))

num = phonenumbers.parse(number, 'RO')
service = carrier.name_for_number(num, 'en')
description = phonenumbers.parse(number, 'CH')
location = geocoder.description_for_number(description, 'en')

opencage_key = '9819eafd9daa47cf8d74fd44b4a121e8'

geolocation = OpenCageGeocode(opencage_key)

location_data = geolocation.geocode(str(location))

latitude = location_data[0]['geometry']['lat']
longitude = location_data[0]['geometry']['lng']

# print data

print('\nService: ' + service)
print('Location: ' + location)

# generate a map

map = folium.Map(location=[latitude,longitude], zoom_start=9)

# add marker to map

folium.Marker([latitude,longitude],popup=location).add_to(map)

# loading bar

print('\nGenerating map\n')

for i in tqdm(range(100)):
    time.sleep(.005)

# generate html file

file_name = 'map.html'
path = os.getcwd() + '//' + file_name

# check if map already exists

if not os.path.exists(path):
    map.save(file_name)
else:
    os.remove(path)
    map.save(file_name)

print('\nMap generated successfully\n')