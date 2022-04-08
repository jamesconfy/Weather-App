from tests import TestWebAppClient

class TestCurrent():
    def test_weather_forecast_get(self):
        response = TestWebAppClient.get('/forecast')

        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'Weather App' in html
        assert 'Submit' in html
        assert 'City' in html
    
    def test_weather_forecast_post(self):
        response = TestWebAppClient.post('/forecast', data={'city': 'Lagos'})

        assert response.status_code == 200
        html = response.get_data(as_text=True)
        
 #       print(html)
        assert 'Current Weather' in html
        assert 'Latitude' in html
        assert 'Longitude' in html
        assert 'Data Receiving Time' in html
        assert 'Wind' in html
        assert 'Temperature' in html
        assert 'Dew Points' in html

    def test_weather_forecast_post_fail(self):
        response = TestWebAppClient.post('/forecast', data={'city': 'Lekki'})
        assert response.status_code == 200
        html = response.get_data(as_text=True)

#        print(html)
        assert '<p>City, Lekki is not found in our database. Please enter another City</p>' in html
        assert 'Weather App' in html
        assert 'Submit' in html