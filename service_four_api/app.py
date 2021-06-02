from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/get_record', methods=['POST'])
def get_record():
    record = str(len(request.data.decode('utf-8'))) 
    finish_type = ['Submission', 'Decision', 'Triangle-Choke', 'Omaplata', 'Gogoplata', 'Eye-Poke']
    finish_type_two = ['KO', 'TKO', 'Drowsiness', 'Fluke']
    return f"{record} wins by {random.choice(finish_type)}"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)