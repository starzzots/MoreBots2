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
import keyboard
SCREEN_SIZE = (0,0,1200,900)
pos_1 = (255,250,0)


def world_hopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presses
    sleep(7.5)
    keyboard.press('f2')# bag hotkey press
    sleep(1)
    keyboard.release('f2')#bag hotkey release
    sleep(2.5)

def main():
    #pg.displayMousePosition()
    center = pg.pixel(502,468)
    if center == pos_1:
        try:
            bank_click = findobjat((0,0,171), SCREEN_SIZE, delta1x=-5,delta2x=-5,delta1y=3,delta2y=3)
            Randomize(bank_click).randleft()
            sleep(7)
        except:
            print("where is the bank?")

     
count = 0
 
while True:
    #count = count + main()
    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
        show_exit_popup()
        sys.exit(0)  # Exit the script when ESC is pressed
        break
    main()
    #if count == 80:
        #world_hopper()
        #count = 0
    