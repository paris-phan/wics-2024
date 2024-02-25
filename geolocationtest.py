from geopy.geocoders import Nominatim

def getGeoLocation(city, country):
    try:
        print("Getting GeoLocation...")
        address = city + ", " + country
        geolocator = Nominatim(user_agent="Geopy Library")

        getLoc = geolocator.geocode(address)

        print(getLoc.address)
        print((getLoc.latitude, getLoc.longitude))
    except:
        
        print("ERROR in getGeoLocation()! give a fuck")


print('wtf')
getGeoLocation("Charlottesville", "United States")