from flask import Flask, request, render_template
import requests
from location import get_location
from weather import get_Weather

# get location
locate = get_location()
my_location = locate['loc']
lat, lon = my_location.split(',')  # Split location string into two numbers

# get weather at location
weather_now = get_Weather(lat,lon)
city = weather_now['name']
province = weather_now['sys']['country']

app = Flask(__name__)

# renders the index.html template
@app.route('/')
def index():
  return render_template('index.html', city = city)


#renders the weather.html template
@app.route('/weather')
def weather():

  # Gets the data from the weather API
  temp = round(weather_now['main']['temp'] - 273.15)
  map = f'https://www.google.ca/maps/place/{lat},{lon}'
  humidity = weather_now['main']['humidity']
  pressure = weather_now['main']['pressure']
  wind = weather_now['wind']['speed']
  description = weather_now['weather'][0]['description'].title()
  return render_template('weather.html', humidity = humidity, pressure = pressure, wind = wind, description = description, temp = temp, city = city, map = map, province = province )

#renders the bmi.html template
@app.route('/bmi', methods = ['GET', 'POST'])
def bmi():
  # Gets the weight and height from the form
  if request.method == 'POST':
    height = request.form['height']
    weight = request.form['weight']
    bm = round(float(weight) / (float(height) * float(height)),2)

    # Assigns the BMI category
    if bm < 18.5:
      bm_status = "Underweight"

    elif bm >= 18.5 and bm < 25:
      bm_status = "Normal"

    elif bm >= 25 and bm < 30:
      bm_status = "Overweight"

    elif bm >= 30:
      bm_status = "Obese"

    # Adds the bmi to a txt file name "promise_file" to keep track of the bmi
    with open('bmi.txt', 'a') as f:
      f.write(f'Height = {height}, Weight = {weight} - BMI = {bm} : {bm_status}\n')




    return render_template('bmi.html', bm = f'Your BMI is: {bm}', bm_status = f'You are: {bm_status}')

  return render_template('bmi.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
