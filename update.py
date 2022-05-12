# import board
# import neopixel
import constants
import getdata
import time

# pixels = neopixel.NeoPixel(board.D18, constants.num_leds)
# pixels.auto_write = True

def update():
    stations = getdata.get_curr_stations()
    for x in stations:
        id = constants.get_station(x[0], x[2])
        color = constants.get_color(x[1].lower()) 
        # pixels[id] = color
        print(id, x[1], color)

update()