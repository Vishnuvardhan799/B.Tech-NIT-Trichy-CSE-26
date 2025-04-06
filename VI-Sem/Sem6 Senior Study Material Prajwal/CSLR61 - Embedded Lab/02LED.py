# import modules
import RPi.GPIO as GPIO
from time import sleep

# setup pins
GPIO.setmode(GPIO.BOARD)
leds = [3, 5, 7]
for led in leds:
    GPIO.setup(led, GPIO.OUT)

while True:
  for led in leds:
    GPIO.output(led, GPIO.HIGH)
    sleep(1)
  for led in leds:
    GPIO.output(led, GPIO.LOW)
    sleep(1)