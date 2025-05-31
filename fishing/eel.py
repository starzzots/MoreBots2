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

#full screen 1920x1080
#67x56
screen_size=(0,0,1920,1080)

running=True
fishing=False
bagfull=False



def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)

def find_finshing_spot():
    fishing_spot_color=(235,20,255)
    try:
        sleep(1.5)
        fishing_click=findobjat(fishing_spot_color,coords=screen_size,delta1x=8,delta2x=12,delta1y=8,delta2y=12)
        Randomize(fishing_click).randleft()
        sleep(16)
    except:
        sleep(1.5)
        fishing_click=findobjat((255,0,221),coords=screen_size,delta1x=8,delta2x=12,delta1y=8,delta2y=12)
        Randomize(fishing_click).randleft()
        sleep(4)


def fishing_check(fishing):
    green=(0,255,0) 
    fishing_color_check = pg.pixel(67,56)
    if fishing_color_check == green:
        fishing = True
        return fishing
    else:
        find_finshing_spot()


def bag_check(bagfull):
    bagcheck=pg.pixel(1587,980)
    last_slot_color=(255,0,0)
    if bagcheck == last_slot_color:
        bagfull = True
        return bagfull
    else:
        bagfull = False
        return bagfull

def dropfish():
    for i in range(26):
        Randomize(bagslotfullscreen[i+3]).shiftclick()
        sleep(.18)

def getscales():
    Randomize(bagslotfullscreen[1]).randleft()
    sleep(1)
    Randomize(bagslotfullscreen[5]).randleft()
    sleep(40)

def main():
    if bag_check(bagfull) == False:
        fishing_check(fishing)
        return 0
    else:
        getscales()
        sleep(1)
        return 1


count = 19
if __name__ == "__main__":
    
    while running:
        sleep(1)
        if count >= 35:
            sleep(40)
            worldhopper()
            count = 0
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
            show_exit_popup()
            sys.exit(0)  # Exit the script when ESC is pressed
            break
        else:
            count= count+ main()