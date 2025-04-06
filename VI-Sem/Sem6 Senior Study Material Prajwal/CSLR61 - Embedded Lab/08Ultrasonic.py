import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trigger = 23
GPIO.setup(trigger, GPIO.OUT)
echo = 24
GPIO.setup(echo, GPIO.IN)

while True:
    GPIO.output(trigger, GPIO.HIGH)
    sleep(0.01)
    GPIO.output(trigger, GPIO.LOW)

    while GPIO.input(echo) == GPIO.LOW:
        start = time()
    while GPIO.input(echo) == GPIO.HIGH:
        end = time()
    
    roundtime = end-start
    dis = round(roundtime*17150, 2)
    print("Distance:", dis, "cm")