from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import db
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app


class TestHome(TestBase):
    def test_S1(self):
        with requests_mock.mock() as m:
            m.get("http://10.154.0.13:5050/").text = ("A","30")
            response = self.client.get(url_for('main'))
    def test_view(self):
        response = self.client.get(url_for('main'))
        self.assertIsNotNone(response.status_code, 200)
        self.assertIsNotNone(response.data)
    