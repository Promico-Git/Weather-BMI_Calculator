import urllib.request, json
import os

# get the weather at a given location
def get_Weather(lat,lon):
  key = os.environ['API_KEY']
  url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result