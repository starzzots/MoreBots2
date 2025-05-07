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
def bank():
    Randomize((844,854,529,535)).randleft()
    sleep(1.6)
    Randomize(bagslotfullscreen[1]).randleft()
    sleep(1)
    Randomize((712,722,496,506)).randleft()
    sleep(1)
    Randomize((715,722,534,543)).randleft()
    sleep(1)
    Randomize((918,927,63,70)).randleft()#exit
    sleep(1)

def makepotion():
    Randomize(bagslotfullscreen[14]).randleft()
    sleep(.2)
    Randomize(bagslotfullscreen[15]).randleft()
    sleep(1.6)
    keyboard.press_and_release('space')
    sleep(1)



if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
        bank()
        makepotion()
        sleep(10)
