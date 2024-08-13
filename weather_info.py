import urllib.request
import json


def get_weather(lat, lon):
    API_KEY = '38cc08e46aa1fd12229524e91e84c96e'
    WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

    request = urllib.request.urlopen(WEATHER_URL, timeout=15)
    response = json.loads(request.read())
    return response

def get_country(lat, lon):
    API_KEY = 'bdc_9b826110ec8744559b072514c71c01aa'
    URL = f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={API_KEY}'

    request = urllib.request.urlopen(URL, timeout=15)
    response = json.loads(request.read())
    return response
