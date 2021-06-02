from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_record(self):
        response = self.client.post(url_for('get_record'), data="name")
        self.assertEqual(response.status_code, 200)
        list = response.data.decode('utf-8').split()
        self.assertEqual(response.data.decode('utf-8')[0], '4')


    def test_two(self):
        string = ""
        for x in range(0, 10):
            
        response = self.client.post(url_for('get_record'), data=string)
        self.assertEqual(response.status_code, 200)
        list = response.data.decode('utf-8').split()
        self.assertEqual(response.data.decode('utf-8')[0], '1')
        
        

       
        
        