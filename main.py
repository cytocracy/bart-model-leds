import board
import neopixel
import constants
import getdata

pixels = neopixel.NeoPixel(board.D18, constants.num_leds)
pixels.auto_write = True

def start():
    
