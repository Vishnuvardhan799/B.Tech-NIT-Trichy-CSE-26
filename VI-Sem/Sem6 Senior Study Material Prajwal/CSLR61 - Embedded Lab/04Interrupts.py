import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 3
GPIO.setup(led, GPIO.OUT)

button = 5
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  GPIO.wait_for_edge(button, GPIO.RISING)
  GPIO.output(led, GPIO.HIGH)
  GPIO.wait_for_edge(button, GPIO.RISING)
  GPIO.output(led, GPIO.LOW)