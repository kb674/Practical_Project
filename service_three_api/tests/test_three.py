from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_martial_art(self):
        response = self.client.get(url_for('get_martial_art'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data.decode('utf-8'),['Wrestling', 'BJJ', 'Judo', 'Submission Grappling', 'Boxing', 'Kickboxing', 'Muay Thai', 'MMA'])