import RPi.GPIO as GPIO
from RPi_LCD import LCD
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

RS, E, D4, D5, D6, D7, BCK = 22, 18, 16, 11, 12, 15, 13
LINES, WIDTH = 2, 16

lcd = LCD(RS, E, D4, D5, D6, D7, BCK, LINES, WIDTH)
lcd.clear()

lcd.display_string("HELLO WORLD", 1)
lcd.display_string("LCD DISPLAY", 2)