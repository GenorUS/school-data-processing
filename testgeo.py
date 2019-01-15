from app import Geocoder
from config import MAPQUEST_API_KEY

geo = Geocoder(MAPQUEST_API_KEY)

res = geo.get_coords("1223 Fox Gap Road", "Bangor", "PA", "18103")
print(res)