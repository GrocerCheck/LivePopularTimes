
import crawler
import os
import json
import livepopulartimes
import requests
import googlemaps
api_key=(open("/home/ihasdapie/keys/gmapkey.txt", 'r')).readline()

#TODO: Create dictionary of stores to PopularTimes/NoData(NULL) : Update every week or so
#TODO: Create updated dictionary of stores to livepopulartines/NoData; Update every 30min

#ChIJbXzc-ohzhlQRIEqmHzSCIKg
#49.239911, -123.125957

a = crawler.get_places_by_search("ChIJbXzc-ohzhlQRIEqmHzSCIKg")

print(a)
