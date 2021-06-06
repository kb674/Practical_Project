from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch


class TestBase(TestCase):
    def create_app(self):
        return app
    
 
class TestHome(TestBase):
    def test_first_name(self):
        response = self.client.get(url_for('get_name'))
        self.assertEqual(response.status_code, 200)
        list = response.data.decode('utf-8').split()
        self.assertIn(list[0],['Paulita', 'Manna', 'Tillie', 'Lamprecht', 'Jayme', 'Fannin', 'Caleb', 'Moris', 'Sideny', 'Monte'])

    def test_nick_name(self):
        response = self.client.get(url_for('get_name'))
        self.assertEqual(response.status_code, 200)
        list = response.data.decode('utf-8').split("'")
        self.assertIn(list[1],["The Beast", "The Dentist", "Beauty and the Beast", "Angel of Death", "Sugar Free", "Ice Cold", "Shogun", "The Thunder", "The Dreamcatcher", "War Machine", "Was a Bullfrog", "Sick Dog", "Cheesesteak", "Cabbage", "Stinkyfeet", "The Word", "Gouda Gouda", "Napao","Lula Molusco", "Toquinho", "Jacare", "Sapo"])
    
    def test_last_name(self):
        response = self.client.get(url_for('get_name'))
        self.assertEqual(response.status_code, 200)
        list = response.data.decode('utf-8').split("'", 3)
        self.assertIn(list[2].strip(),['Coombs', 'Gallows', 'Franzoni', 'Hoeppner', 'Costello', 'Scotti', 'Mellor', 'Lowenstein', 'Merino', 'Portier'])

    
    

        
