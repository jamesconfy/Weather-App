from tests import TestWebAppClient

class TestCurrent():
    def test_current_weather_get(self):
        response = TestWebAppClient.get('/current')

        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'Weather App' in html
        assert 'Submit' in html
        assert 'City' in html
    
    def test_current_weather_post(self):
        response = TestWebAppClient.post('/current', data={'city': 'Lagos'})

        assert response.status_code == 200
        html = response.get_data(as_text=True)
        
        assert 'Current Weather' in html
        assert 'Latitude' in html
        assert 'Longitude' in html
        assert 'Data Receiving Time' in html
        assert 'Wind' in html
        assert 'Temperature' in html
        assert 'Sea Level' in html

    def test_current_weather_post_fail(self):
        response = TestWebAppClient.post('/current', data={'city': 'Lekki'})
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert '<p>City, Lekki is not found in our database. Please enter another City</p>' in html
        assert 'Weather App' in html
        assert 'Submit' in html