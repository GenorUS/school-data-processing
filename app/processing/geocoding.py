import requests
from urllib.parse import urlencode, unquote, urlparse, parse_qsl, ParseResult, quote
import json


class Geocoder(object):
    def __init__(self, api_key):
        self.base_url = 'https://www.mapquestapi.com/geocoding/v1/address?'
        self.api_key = api_key


    def get_coords(self, street: str, city: str, state: str, zipcode: str) -> str:
        loc_dict = {
            "street": quote(street),
            "city": quote(city),
            "state": quote(state),
            "postalCode": zipcode
        }
        
        req_dict = {
            "location": loc_dict,
            "options": {
                "thumbMaps": "false"
            }
        }

        req_json = json.dumps(req_dict)
        full_url = "{}key={}&inFormat=json&outFormat=json&json={}".format(self.base_url, self.api_key, req_json)
        res = requests.get(full_url).json()
        coords = res['results'][0]['locations'][0]['latLng']
        return coords





