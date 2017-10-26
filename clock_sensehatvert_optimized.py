from datetime import datetime
from sense_hat import SenseHat
from time import sleep

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear = (0, 0, 0)

# minutes
minutes = {
    0: (0, 3),
    1: (1, 3),
    2: (2, 3),
    3: (3, 3),
    4: (0, 4),
    5: (1, 4),
    6: (2, 4),
    7: (3, 4),
    8: (0, 5),
    9: (1, 5),
    10: (2, 5),
    11: (3, 5),
    12: (0, 6),
    13: (1, 6),
    14: (2, 6),
    15: (3, 6),
    16: (0, 7),
    17: (1, 7),
    18: (2, 7),
    19: (3, 7),
    }
#comment
def getPixelsForTime(dt):
    hours = dt.hour
    minutes = int(dt.minute / 3)
    seconds = int(dt.second / 3)
    pixels = []
    for x in range (0, hours + 1):
        pixels.append(red)
    for x in range (hours + 1, 24):
        pixels.append(clear)
    for x in range (0, 40):
        if (x >= 0 and x < 4) or (x >= 8 and x < 12) or (x >= 16 and x < 20) or (x >= 24 and x < 28) or (x >= 32 and x < 36):
            if (int(x / 2) <= minutes):
                pixels.append(green)
            else:
                pixels.append(clear)
        if (x >= 4 and x < 8) or (x >= 12 and x < 16) or (x >= 20 and x < 24) or (x >= 28 and x < 32) or (x >= 36 and x < 40): 
            if int(x / 2) <= seconds:
                pixels.append(blue)
            else:
                pixels.append(clear)
    return pixels
        

def clearSeconds():
    for y in range (3, 8):
        for x in range (4, 8):
            sense.set_pixel(x, y, clear)

def clearMinutes():
    for y in range (3, 8):
        for x in range (0, 4):
            sense.set_pixel(x, y, clear)

def clearHours():
    for y in range(0, 4):
        for x in range(0, 8):
            sense.set_pixel(x, y, clear)

def updateSeconds(sense, s):
    secondsLookup = int(s / 3)
    sense.set_pixel(minutes[secondsLookup][0] + 4, minutes[secondsLookup][1], blue)
        
def updateMinutes(sense, m):
    minutesLookup = int(m / 3)
    sense.set_pixel(minutes[minutesLookup][0], minutes[minutesLookup][1], green)

def updateHours(sense, h):
    sense.set_pixel((h % 8), int(h / 8), red)
    
sense = SenseHat()
sense.clear()
MyDateTime = datetime.now()
pixels = getPixelsForTime(MyDateTime)
sense.set_pixels(pixels)
while True:
    MyDateTime = datetime.now()
    updateSeconds(sense, MyDateTime.second)
    if (MyDateTime.second == 0):
        clearSeconds()
        updateMinutes(sense, MyDateTime.minute)
        if (MyDateTime.minute == 0):
            clearMinutes()
            updateHours(sense, MyDateTime.hour)
            if (MyDateTime.hour == 0):
                clearHours()
    sleep(1)
