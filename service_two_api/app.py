from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/get_name', methods=['GET'])
def get_name():
    first_name = ['Paulita', 'Manna', 'Tillie', 'Lamprecht', 'Jayme', 'Fannin', 'Caleb', 'Moris', 'Sideny', 'Monte']
    last_name = ['Coombs', 'Gallows', 'Franzoni', 'Hoeppner', 'Costello', 'Scotti', 'Mellor', 'Lowenstein', 'Merino', 'Portier']
    nick_name = ["The Beast", "The Dentist", "Beauty and the Beast", "Angel of Death", "Sugar Free", "Ice Cold", "Shogun", "The Thunder", "The Dreamcatcher", "War Machine", "Was a Bullfrog", "Sick Dog", "Cheesesteak", "Cabbage", "Stinkyfeet", "The Word", "Gouda Gouda"]
    nick_name_two = ['Napao', 'Lula Molusco', 'Toquinho', 'Jacare', 'Sapo']
    fighter_name = f"{random.choice(first_name)} '{random.choice(nick_name_two)}' {random.choice(last_name)}"
    return fighter_name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)