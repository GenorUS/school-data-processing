from app import Geocoder
from config import MAPQUEST_API_KEY, MAPQUEST_SECRET

geo = Geocoder(MAPQUEST_API_KEY, MAPQUEST_SECRET)

res = geo.get_coords("1701 JFK Blvd", "Philadelphia", "PA", "19103")
print(res)