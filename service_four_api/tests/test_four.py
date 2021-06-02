from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_record(self):
        string = "nameArt"
        response = self.client.post(url_for('get_record'), data=string)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8')[0], str(len(string)) )

    def test_get_record_two(self):
        test_cases = ["PaulitaWrestling", "ShoshanaBJJ", "JaymeJudo"]
        for each_case in test_cases:
            string = each_case
            response = self.client.post(url_for('get_record'), data=string)
            record = str(len(string)) 
            self.assertEqual(response.data.decode('utf-8')[0:2].strip(), (record) )






    
        
        

       
        
        