from datetime import datetime
from sense_hat import SenseHat
from time import sleep

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear = (0, 0, 0)

def getpixelsfortime(dt):
    hours = dt.hour
    minutes = int(dt.minute / 1.5)
    seconds = int(dt.second / 8)
    r = red
    g = green
    b = blue
    c = clear 
    pixels = []
    for x in range(0, hours):
        pixels.append(r)
    for x in range (hours, 16):
        pixels.append(c)
    for x in range (0, minutes):
        pixels.append(g)
    for x in range (minutes, 40):
        pixels.append(c)
    for x in range(0, seconds):
        pixels.append(b)
    for x in range(seconds, 8):
        pixels.append(c)
        
    return pixels

sense = SenseHat()
sense.clear()
while True:
    MyDateTime = datetime.now()
    pixels = getpixelsfortime(MyDateTime)
    sense.set_pixels(pixels)
    sleep(8)
