from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    fighter_name = requests.get('http://service_two_api:5000/get_name')
    martial_art = requests.get('http://service_two_api:5000/get_martial_art')
    return render_template('index.html', fighter_name=fighter_name.text, martial_art=martial_art.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)