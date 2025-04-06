from adafruit_dht import DHT22
import board
from time import sleep

dht = DHT22(board.D22)

while True:
    try:
        t = dht.temperature
        h = dht.humidity
        if t is not None and h is not None:
            print("Temperature =", t, "and Humidity =", h, "%")
        else:
            print("Failed to retrieve readings correctly !")
    except RuntimeError as error:
        print(error.args[0])
    sleep(2)