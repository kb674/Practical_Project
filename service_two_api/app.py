from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def get_name():
    first_name = ['Shoshana', 'Kimbery', 'Ara', 'Joellen', 'Cecile']
    last_name = ['Lazzaro', 'Kubik', 'Macneil', 'Vizcarrondo', 'Martine']
    nick_name = ['Cabbage', 'Chainsaw', 'War Machine', 'Hands of Steel', 'Meathead']
    fighter_name = f"{random.choice(first_name)} '{random.choice(nick_name)}'' {random.choice(last_name)}"
    return fighter_name

@app.route('/get_martial_art', methods=['GET'])
def get_martial_art():
    grappling = ['Wrestling', 'BJJ', 'Judo', 'Submission Grappling']
    striking = ['Boxing', 'Kickboxing', 'Muay Thai', 'MMA']
    return random.choice(grappling)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)