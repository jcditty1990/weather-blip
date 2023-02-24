from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def get_weather(city):
    api_key = '27fce5eaff60808f09684d15c0099b1f'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    return data


@app.route('/', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    return render_template('weather.html', temperature=temperature, description=description)


#export FLASK_APP=app.py
#flask run


if __name__ == '__main__':
    app.run()