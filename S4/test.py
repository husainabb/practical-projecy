from flask_testing import TestCase
from flask import url_for
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrize(TestBase):
    def test_prize_creator(self):
        response = self.client.get(url_for('result'))
        self.assertEqual(response.status_code, 500)