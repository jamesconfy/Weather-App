from flask import Flask, render_template, url_for, request, redirect
import requests
import os
from forms import CurrentWeatherForm
from utils import ms_to_date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hafdgjhluerhadj'
BASE_URL = 'http://api.openweathermap.org/data/2.5'
API_KEY = os.environ.get('API_key')


@app.route('/')
@app.route('/home')
async def home():
    return render_template("home.html")


@app.route('/current', methods=['POST', 'GET'])
async def current():
    form = CurrentWeatherForm()
    if request.method == 'POST':
        city = form.city.data
        try:
            #API_key = os.environ.get('API_key')
            API_key = '50d0ca8e106821a32b9361d45bb7f16a'
            api = requests.get(f'{BASE_URL}/weather?q={city}&appid={API_key}')
            data = api.json()
            #return data
            dt = ms_to_date(data.get("dt"), data.get("timezone"))
            sr = ms_to_date(data["sys"]["sunrise"], data.get("timezone"))
            ss = ms_to_date(data["sys"]["sunset"], data.get("timezone"))
            return render_template('view_data.html', data=data, title="Current Weather", legend='Current Weather', dt=dt, sr=sr, ss=ss)

        except requests.exceptions.ConnectionError as err:
            return f'Error: {err}'

        except requests.exceptions.HTTPError as err:
            return f'Error: {err}'

    return render_template('current.html', form=form, title='Current Weather')

@app.route('/forecast', methods=['POST', 'GET'])
async def forecast():
    form = CurrentWeatherForm()
    if request.method == 'POST':
        city = form.city.data
        try:
            #API_key = os.environ.get('API_key')
            API_key = 'd228a089b08406745e52568262b60f83'
            api1 = requests.get(f'{BASE_URL}/weather?q={city}&appid={API_key}')
            data1 = api1.json()
            lat = data1['coord']['lat']
            lon = data1['coord']['lon']

            api = requests.get(f'{BASE_URL}/onecall?lat={lat}&lon={lon}&&appid={API_key}')
            data = api.json()
            return data
            dt = ms_to_date(data.get("dt"), data.get("timezone_offset"))
            sr = ms_to_date(data["sys"]["sunrise"], data.get("timezone_offset"))
            ss = ms_to_date(data["sys"]["sunset"], data.get("timezone_offset"))
            return render_template('view_data.html', data=data, title="Current Weather", legend='Current Weather', dt=dt, sr=sr, ss=ss)

        except requests.exceptions.ConnectionError as err:
            return f'Error: {err}'

        except requests.exceptions.HTTPError as err:
            return f'Error: {err}'

    return render_template('forecast.html', form=form, title='Weather Forecast')


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="localhost")
