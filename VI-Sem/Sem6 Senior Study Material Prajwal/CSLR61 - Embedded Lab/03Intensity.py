import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 3
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 100)
pwm.start(0)

while True:
  for i in range(100):
    pwm.ChangeDutyCycle(i)
    sleep(0.01)
  for i in range(100, 0, -1):
    pwm.ChangeDutyCycle(i)
    sleep(0.01)