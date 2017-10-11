from datetime import datetime
from sense_hat import SenseHat
from time import sleep

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear = (0, 0, 0)

def getpixelsfortime(dt):
    hours = dt.hour
    minutes = int(dt.minute * 2 / 3)
    seconds = int(dt.second * 2 / 3)
    r = red
    g = green
    b = blue
    c = clear 
    pixels = []
    for x in range(0, hours):
        pixels.append(r)
    for x in range (hours, 24):
        pixels.append(c)

    for x in range (0, 40):
        if (x >= 0 and x < 4) or (x >= 8 and x < 12) or (x >= 16 and x < 20) or (x >= 24 and x < 28) or (x >= 32 and x < 36):
            if x <= minutes:
                pixels.append(g)
            else:
                pixels.append(c)
        if (x >= 4 and x < 8) or (x >= 12 and x < 16) or (x >= 20 and x < 24) or (x >= 28 and x < 32) or (x >= 36 and x < 40): 
            if x <= seconds:
                pixels.append(b)
            else:
                pixels.append(c)
    return pixels

sense = SenseHat()
sense.clear()
while True:
    MyDateTime = datetime.now()
    pixels = getpixelsfortime(MyDateTime)
    sense.set_pixels(pixels)
    sleep(2 / 3)
