import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address?"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops?"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "bJbmdtoWySA9wyCsDz4WdsAhGYR8rddq"
MBTA_API_KEY = "5bfc58214dae44fba3eafc1fe0af144c"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    data = {'key': MAPQUEST_API_KEY, 'location': place_name}
    para = urllib.parse.urlencode(data)
    result = get_json(MAPQUEST_BASE_URL + para)
    result_lat_long = result["results"][0]["locations"][0]['latLng']
    latitude, longitude = result_lat_long['lat'], result_lat_long['lng']
    return latitude, longitude


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    data = {'filter[latitude]': latitude, 'filter[longitude]': longitude}
    para = urllib.parse.urlencode(data)
    result = get_json(MBTA_BASE_URL + para)
    result_stop = result['data'][0]['attributes']['name']
    result_wheelchair = result['data'][0]['attributes']['wheelchair_boarding']
    if result_wheelchair == 0:
        wheelchair = 'Do not know if this station is wheelchair accessible or not.'
    elif result_wheelchair == 1:
        wheelchair = 'This station is wheelchair accessible.'
    else:
        wheelchair = 'Wheelchair is inaccessible at this station.'
    return result_stop, wheelchair


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    return get_nearest_station(get_lat_long(place_name)[0],get_lat_long(place_name)[1])

def main():
    """
    You can all the functions here
    """
    print(get_lat_long('21 Babson College Drive'))
    print(get_nearest_station('42.3539038', '-71.1337112'))
    print(find_stop_near('181 Brighton Ave, Allston, MA 02134'))


if __name__ == '__main__':
    main()

