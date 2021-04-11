from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from flask import url_for
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRanLetterGenerator(TestBase):
    def test_ranlettergenerator(self):
        response = requests.get(url_for('RanLetterGenerator')).text
        response = str(response)
        self.assertEqual(len(response), 1)

class TestRanLetterGen(TestBase):
    def test_ranlettergen(self):
        response = self.client.get(url_for('RanLetterGenerator'))
        self.assertEqual(response.status_code, 200)