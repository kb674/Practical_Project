from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    art = db.Column(db.String(50), nullable = False)
    record = db.Column(db.String(100), nullable = False)

@app.route('/')
def home():
    fighter_name = requests.get('http://service_two_api:5000/get_name')
    martial_art = requests.get('http://service_three_api:5000/get_martial_art')
    record = requests.post('http://service_four_api:5000/get_record', data=(fighter_name.text + martial_art.text))
    
    
    all_profiles = Fighters.query.all()

    latest_profile = Fighters(name=fighter_name.text, art=martial_art.text, record=record.text)
    db.session.add(latest_profile)
    db.session.commit()

    return render_template('index.html', title='Home', all_profiles=all_profiles, latest_profile=latest_profile)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
