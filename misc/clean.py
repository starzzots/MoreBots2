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


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
            break
        Randomize((844,854,529,535)).randleft()
        sleep(1.6)
        Randomize(bagslotfullscreen[1]).randleft()
        sleep(1)
        Randomize((762,771,572,578)).randleft()
        sleep(1)
        Randomize((918,927,63,70)).randleft()
        sleep(1)
        for i in range(28):
            Randomize(bagslotfullscreen[i+1]).randleftspeed()
            sleep(.02)
        sleep(1)