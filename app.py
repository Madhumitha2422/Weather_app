import requests
from flask import Flask, render_template, request
from liveserver import LiveServer

app = Flask(__name__)

ls = LiveServer(app)


API_KEY = "4282ed3046a0092fd0bc635043617b2b"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if weather_data:
            return render_template('index.html', data=weather_data,city_name=city)
        else:
            return "City not found"
    return ls.render_template('index.html')

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data.get("cod") == "200":
        

            forecast = data['list'][:]
            return forecast
        else:
            return None
    except requests.exceptions.RequestException:
        return None

if __name__ == 'main':
    ls.run(debug=True)