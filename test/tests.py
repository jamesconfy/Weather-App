import unittest
from flask import current_app
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/mac/Downloads/Python Projects/weather-app/')
from weather_app import create_app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.app.config.update({'WTF_CSRF_ENABLED': False})
        self.appctx.push()

        return self.app

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def test_app(self):
       assert self.app is not None
       assert current_app == self.app

TestWebAppClient = TestWebApp().setUp().test_client()