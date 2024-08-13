from flask import Flask,render_template,request
import json
from weather_info import get_country,get_weather
app = Flask(__name__)



#Default page
#Have to write the data into the json file to get the data 
@app.route('/', methods = ['GET','POST'])
def index():
  #Getting user lat and lon
  user_lat = None
  user_lon = None
  if request.method == 'POST':
    data = request.json
    data_response = json.loads(data)
    with open('static/user_loc.json', 'w') as f:
        json.dump(data_response, f)
  f_open = open('static/user_loc.json','r')
  get_data = json.loads(f_open.read())
  user_lat = get_data['lat']
  user_lon = get_data['lon']
  
  weather_data= get_weather(user_lat,user_lon)
  temp,humid = weather_data['main']['temp'],weather_data['main']['humidity']
  temp_celcius = round(temp - 272.15,2)
  location_data = get_country(user_lat,user_lon)
  country_name,country_city = location_data['countryName'],location_data['city']
  return render_template('index.html',lat = user_lat,lon=user_lon,city=country_city,country=country_name,temp=temp_celcius,humid = humid)

#Project page
@app.route('/projects/')
def projects():
  return render_template('projects.html')

#Resume page
@app.route('/resume/')
def resume():
  return render_template('resume.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)