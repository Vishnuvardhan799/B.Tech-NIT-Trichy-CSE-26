from flask import Flask, render_template
from flask_cors import CORS

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led = 3
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/e')
def e():
    GPIO.output(led, GPIO.HIGH)
    return "Light Turned ON !"

@app.route('/d')
def d():
    GPIO.output(led, GPIO.LOW)
    return "Light Turned OFF !"

app.config['CORS_HEADERS'] = 'Content-Type'
if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = '127.0.0.1')