# wsgi.py
from datetime import datetime
from flask import Flask, jsonify
from dice_roller.dice import Dice

app = Flask(__name__)
print("hop")
@app.route('/')
def home():
    dice = Dice()
    return jsonify({
        'roll': dice.roll(),
        'timestamp': datetime.now()
    })
