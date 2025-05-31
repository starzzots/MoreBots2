import sys
import os


# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the MoreBots2 folder dynamically (parent directory of the current script)
morebots_path = os.path.abspath(os.path.join(current_dir, '..'))  # Move up one level from the script's directory

# Add MoreBots2 to sys.path
if morebots_path not in sys.path:
    sys.path.insert(0, morebots_path)

# Now you can import from tools without hardcoding the path
from tools.windowcapture import WindowCapture
from tools.clicks import *
from tools.tools import *
from time import time, sleep
farmer_color=(255,0,221)
pg.PAUSE = 0
def steal(obj_color):
    farmer_location=findobjat(obj_color, delta1x = 0, delta2x=0,delta1y=12,delta2y=12)
    return farmer_location

def drop_garbage():
    for i in bagslotfullscreen:
        if pg.pixel(bagslotfullscreen[i][0], bagslotfullscreen[i][-1]) == (255,0,0):
            sleep(.04)
            Randomize(bagslotfullscreen[i]).shiftclick()
def eat():
    for i in bagslotfullscreen:
        if pg.pixel(bagslotfullscreen[i][0], bagslotfullscreen[i][-1]) == (114,16,160):
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            sleep(1.6)
            Randomize(bagslotfullscreen[i]).uniclick()
            break
    



    
while True:
    if keyboard.is_pressed('q'):
        sys.exit()
        break
    if pg.pixel(bagslotfullscreen[14][0], bagslotfullscreen[14][-1]) == (255,0,0):
        drop_garbage()
    elif pg.pixel(1419,916) != (122,27,8):
        eat()
    else:
        
        Randomize(steal(farmer_color)).uniclick()
