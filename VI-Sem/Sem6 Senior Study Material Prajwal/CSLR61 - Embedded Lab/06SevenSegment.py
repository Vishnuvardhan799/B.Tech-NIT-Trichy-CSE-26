import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leds = [19, 21, 22, 23, 24, 26, 28]
for led in leds:
    GPIO.setup(led, GPIO.OUT)

M = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
] # 7-segment display matrix

n = 0
while True:
    for led in leds:
        GPIO.output(led, GPIO.LOW)
    for i in range(8):
        if M[n][i] == 1:
            GPIO.output(leds[i], GPIO.HIGH)
    sleep(1)
    n = (n+1) % 10