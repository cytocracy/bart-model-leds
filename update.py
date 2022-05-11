import board
import neopixel
import constants
import getdata
import time

pixels = neopixel.NeoPixel(board.D18, constants.num_leds)
pixels.auto_write = True

def update():
    stations = getdata.get_curr_stations()
    for x in stations:
        pixels[constants.getstation(x[0], x[2])] = constants.getcolor(x[1])

update()