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
def drop():
    for i in bagslotfullscreen:
        if pg.pixel(bagslotfullscreen[i][0], bagslotfullscreen[i][-1]) == (255,0,0):
            sleep(.04)
            Randomize(bagslotfullscreen[i]).shiftclick()
def bot():
    stall_position = pg.pixel(818,516)#255,115,0
    if stall_position == (255,115,0):
        Randomize((805,809,525,532)).randleft()
    if pg.pixel(bagslotfullscreen[28][0], bagslotfullscreen[28][-1]) == (255,0,0):
        drop()
while True:

    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
        show_exit_popup()
        sys.exit(0)  # Exit the script when ESC is pressed
        break
    bot()