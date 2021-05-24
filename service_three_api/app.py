from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_martial_art', methods=['GET'])
def get_martial_art():
    grappling = ['Wrestling', 'BJJ', 'Judo', 'Submission Grappling']
    striking = ['Boxing', 'Kickboxing', 'Muay Thai', 'MMA']
    return random.choice(grappling)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)