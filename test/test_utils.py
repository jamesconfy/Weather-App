from tests import TestWebAppClient
from flask import current_app, session
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/mac/Downloads/Python Projects/Weather-App/')
from weather_app.utils import ms_to_date

class TestUtils():
    def test_utils(self):
        result = ms_to_date(1000, 12)
        assert str(result) == "1970-01-01 01:16:28"

        result = ms_to_date(10, 120)
        assert str(result) == "1970-01-01 00:58:10"