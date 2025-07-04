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
pos_1 = (0,0,1)
pos_2 = (0,0,2)
pos_3 = (0,0,3)
pos_4 = (0,0,4)
pos_5 = (0,0,5)
pos_6 = (0,0,6)
pos_7 = (0,0,7)
pos_8 = (255,255,0)
fail1 = (0,0,10) 
fail_2 = (0,0,9)


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
    sleep(1)
    center = pg.pixel(503,459)
    #print(center)


    if center == pos_1:
        if pg.pixel(470,441) == (205,0,0):
            Randomize((476,478,440,441)).randleft()
            sleep(2.6)
            Randomize((405,413,438,455)).randleft()
            return 0
        else:
            Randomize((381,387,407,427)).randleft()
            return 0
    elif center == fail1:
        Randomize((687,694,530,534)).randleft()
        return 0
    elif center == fail_2:
        Randomize((763,766,397,398)).randleft()
        return 0
    elif center == pos_2:
        if pg.pixel(444,483) == (205,0,0):
            Randomize((448,452,477,481)).randleft()
            sleep(3)
            Randomize((512,517,517,520)).randleft()
            return 0
        elif pg.pixel(404,479) == (205,0,0):
            Randomize((409,411,478,480)).randleft()
            sleep(3.5)
            Randomize((553,558,518,520)).randleft()
            sleep(1)
            return 0
        else:
            Randomize((459,465,535,539)).randleft()
            return 0
    elif center == pos_3:
        sleep(2)
        if pg.pixel(528,448) == (205,0,0) or pg.pixel(528,448) == (203,0,0):
            Randomize((527,530,453,455)).randleft()
            sleep(2)
            Randomize((478,498,528,535)).randleft()
            sleep(3)
            return 0
        else:    
            Randomize((499,535,522,531)).randleft()
            sleep(4)
            return 0
    
    elif center == pos_4:
        
        Randomize((369,398,502,511)).randleft()
        sleep(4.5)
        return 1
    
    elif center == pos_5:

        if pg.pixel(444,465) == (205,0,0):
            Randomize((448,451,467,468)).randleft()
            sleep(2.6)
            Randomize((566,575,487,496)).randleft()
            sleep(3)
            return 0
        else:
            #check for token last spot
            Randomize((512,518,481,495)).randleft()
            sleep(2)
            return 0
    elif center == pos_6:
        Randomize((771,773,311,312)).randleft()
        return 0
    
    elif center == pos_7:
        Randomize((554,558,278,288)).randleft()
        return 0
    
    elif center == pos_8:
        Randomize((348,353,503,509)).randleft()
        return 0
    else:
        return 0
    
counter=0

if __name__ == "__main__":
    while True:
        sleep(1.5)
        if counter == 70:
            worldhopper()
            counter = 0
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
            show_exit_popup()
            sys.exit(0)  # Exit the script when ESC is pressed
            break
        else:
            counter=counter+main()