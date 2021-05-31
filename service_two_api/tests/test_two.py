from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_name(self):
        response = self.client.get(url_for('get_name'))
        self.assertEqual(response.status_code, 200)

        with patch ('random.choice') as r:
            r.return_value = 'Shoshana'
        
        response.data = r.return_value
        self.assertIn(b'Shoshana', response.data)