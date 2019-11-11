import urllib.request
import urllib.parse


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "bJbmdtoWySA9wyCsDz4WdsAhGYR8rddq"


params = urllib.parse.urlencode({'key': MAPQUEST_API_KEY, 'location': 'BabsonCollege'})
url = MAPQUEST_BASE_URL % params
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))