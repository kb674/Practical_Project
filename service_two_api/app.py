from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_name', methods=['GET'])
def get_name():
    first_name = ['Paulita', 'Manna', 'Tillie', 'Lamprecht', 'Jayme', 'Fannin', 'Caleb', 'Moris', 'Sideny', 'Monte']
    last_name = ['Coombs', 'Gallows', 'Franzoni', 'Hoeppner', 'Costello', 'Scotti', 'Mellor', 'Lowenstein', 'Merino', 'Portier']
    nick_name = ["The Beast", "The Dentist", "Beauty and the Beast", "Angel of Death", "Sugar Free", "Ice Cold", "Shogun", "The Thunder", "The Dreamcatcher", "War Machine", "Was a Bullfrog", "Sick Dog", "Cheesesteak", "Cabbage", "Stinkyfeet", "The Word", "Gouda Gouda"]
    nick_name_two = ['Napao', 'Lula Molusco', 'Toquinho', 'Jacare', 'Sapo']
    fighter_name = f"{random.choice(first_name)} '{random.choice(nick_name)}'' {random.choice(last_name)}"
    return fighter_name

@app.route('/get_martial_art', methods=['GET'])
def get_martial_art():
    grappling = ['Wrestling', 'BJJ', 'Judo', 'Submission Grappling']
    striking = ['Boxing', 'Kickboxing', 'Muay Thai', 'MMA']
    return random.choice(grappling)

@app.route('/get_record', methods=['POST'])
def get_record():
    record = str(len(request.data.decode('utf-8')))
    finish_type = ['Submission', 'Decision', 'Triangle Choke', 'Omaplata', 'Gogoplata', 'Eye Poke']
    finish_type_two = ['KO', 'TKO', 'Drowsiness', 'Fluke']
    return f"{record} wins by {random.choice(finish_type)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)