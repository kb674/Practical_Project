from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app, db
from app import Fighters

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db")
        return app
    
    def Set_up(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.mock() as mocker:
            mocker.get('http://service_two_api:5000/get_name', text='name')
            mocker.get('http://service_three_api:5000/get_martial_art', text='Judo')
            mocker.post('http://service_four_api:5000/get_record', text='45 wins by Submission')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'name', response.data)
            self.assertIn(b'Judo', response.data)
