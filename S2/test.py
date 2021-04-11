from app import app
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNumbers(TestBase):
    def test_numbers(self):
        response = self.client.get(url_for('NumGenerator'))
        self.assertEqual(len(response.data), 1)

    
class TestRandomNumberGen(TestBase):    
    def test_letters(self):         
            response = self.client.get(url_for('NumGenerator'))
            self.assertIn(response.status_code, 200)