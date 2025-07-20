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

#200 zoom
pos1=(0,0,1)
pos2=(0,0,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,5)
pos6=(0,0,6)
pos7=(0,0,7)
fail1=(0,0,9)
fail2=(0,0,10)
tokenc=(205,0,0)

def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)
def main():
    center=pg.pixel(502,462)
    #print(center)
    if center == pos1:
        #token1 here
        if pg.pixel(474,481) == (129,108,7):
            Randomize((474,477,478,482)).randleft()
            sleep(2)
            Randomize((493,500,519,527)).randleft()
            sleep(4.3)
        else:
            Randomize((448,464,537,553)).randleft()
            sleep(5)
    elif center == fail1:
        Randomize((515,519,174,177)).randleft()
        sleep(10.5)
    elif center == pos2:
        Randomize((514,518,594,603)).randleft()
        sleep(8.5)
    elif center == pos3:
        #token 2 and 3 here
        if pg.pixel(509,495) == (205,0,0):
            Randomize((513,517,491,495)).randleft()
            sleep(2.6)
            Randomize((516,532,402,414)).randleft()
            sleep(10.5)
        elif pg.pixel(523,479) == (205,0,0):
            Randomize((528,530,477,482)).randleft()
            sleep(2.3)
            Randomize((504,523,416,427)).randleft()
            sleep(10.5)
        else:
            Randomize((531,549,428,439)).randleft()
            sleep(10.5)
    elif center == pos4:
        #token 4 and 5 here
        if pg.pixel(528,508) == (129,108,7):
            Randomize((528,531,507,509)).randleft()
            sleep(2.6)
            Randomize((529,539,406,412)).randleft()
            sleep(4.5)
        elif pg.pixel(538,494) == (205,0,0):
            Randomize((541,545,493,496)).randleft()
            sleep(2.6)
            Randomize((515,524,419,427)).randleft()
            sleep(4)
        else:
            Randomize((555,561,441,449)).randleft()
            sleep(4.5)
    elif center == pos5:
        Randomize((552,558,383,392)).randleft()
        sleep(9.3)
    elif center == pos6:
        Randomize((481,494,374,388)).randleft()
        sleep(5)
    elif center == pos7:
        Randomize((304,305,441,443)).randleft()
        sleep(7)
        Randomize((348,349,481,482)).randleft()
        sleep(6)
    

if __name__ == "__main__":
    counter=0
    while True:
        sleep(1.5)
        main()
        if counter >= 200:
            worldhopper()
            counter = 0
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
            show_exit_popup()
            sys.exit(0)  # Exit the script when ESC is pressed
            break