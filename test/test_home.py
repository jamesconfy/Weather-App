from tests import TestWebAppClient

class TestHome():
    def test_home(self):
        response = TestWebAppClient.get('/' or '/home')

        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert "Home" in html
        assert "Check" in html
        assert "Weather" in html
        assert "Current" in html
        assert "Forecast" in html
