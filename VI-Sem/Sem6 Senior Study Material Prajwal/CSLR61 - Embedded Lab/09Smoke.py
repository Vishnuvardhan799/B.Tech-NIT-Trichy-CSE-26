import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

smoke = 7
GPIO.setup(smoke, GPIO.IN)

while True:
    level = GPIO.input(smoke)
    print("Smoke Level:", level)
    sleep(1)