import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pir = 17
GPIO.setup(pir, GPIO.IN)

while True:
    if GPIO.input(pir):
        print("Motion Detected")
    else:
        print("No Motion Detected")
    sleep(1)