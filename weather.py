from flask import Flask, render_template, request, flash
import requests
import os
from forms import CurrentWeatherForm
from utils import ms_to_date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hafdgjhluerhadj'
BASE_URL = 'http://api.openweathermap.org/data/2.5'
API_key = os.environ.get('API_key')

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
            api = requests.get(f'{BASE_URL}/weather?q={city}&appid={API_key}')
            data = api.json()
            if data["cod"] != "404":

                dt = ms_to_date(data.get("dt"), data.get("timezone"))
                sr = ms_to_date(data["sys"]["sunrise"], data.get("timezone"))
                ss = ms_to_date(data["sys"]["sunset"], data.get("timezone"))
                return render_template('view_data_current.html', data=data, title="Current Weather", legend='Current Weather', dt=dt, sr=sr, ss=ss)

        except requests.exceptions.ConnectionError as err:
            return f'Error: {err}'

        except requests.exceptions.HTTPError as err:
            return f'Error: {err}'
        
        flash(f'City, {city} is not found in our database. Please enter another City', 'danger')
    return render_template('current.html', form=form, title='Current Weather')

@app.route('/forecast', methods=['POST', 'GET'])
async def forecast():
    form = CurrentWeatherForm()
    if request.method == 'POST':
        city = form.city.data
        try:
            api1 = requests.get(f'{BASE_URL}/weather?q={city}&appid={API_key}')
            data1 = api1.json()
            if data1["cod"] != "404":

                lat = data1['coord']['lat']
                lon = data1['coord']['lon']
                part = "daily,hourly"
                unit = "metric"

                api = requests.get(f'{BASE_URL}/onecall?lat={lat}&lon={lon}&units={unit}&exclude={part}&appid={API_key}')
                data = api.json()

                dt = ms_to_date(data["current"]["dt"], data.get("timezone_offset"))
                sr = ms_to_date(data["current"]["sunrise"], data.get("timezone_offset"))
                ss = ms_to_date(data["current"]["sunset"], data.get("timezone_offset"))
                return render_template('view_data_fore.html', data=data, title="Current Forecast", legend='Forecast Weather', dt=dt, sr=sr, ss=ss)

        except requests.exceptions.ConnectionError as err:
            return f'Error: {err}'

        except requests.exceptions.HTTPError as err:
            return f'Error: {err}'

        flash(f'City, {city} is not found in our database. Please enter another City', 'danger')
    return render_template('forecast.html', form=form, title='Weather Forecast')


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="localhost")
