import urllib.request
import json

# Automatically geolocate the connecting IP
def get_location():
  url = "https://ipinfo.io/json"
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result