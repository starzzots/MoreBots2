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
STUCK_STATE = (0,2,0)
pos_1 = (255,250,0)
pos_2=(73,64,52)
pos_3=(0,1,0)
pos_4 = (0,2,0)
pos_5 = (25,3,0)
pos_6 = (0,4,0)
pos_7 = (0,5,0)
pos_8 = (0,8,0)
pos_9 = (0,9,0)



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
    STUCK_STATE = (0,2,0)
    center = pg.pixel(502,468)
    #pg.displayMousePosition()
    #print(center)
    if pg.pixel(944,640) != (53,53,255):
        Randomize((904,908,630,632)).randleft()
        sleep(.2)
        return 0
    if STUCK_STATE == pos_4:
        if center == pos_1:
            STUCK_STATE = pos_4
            try:
                bank_click = findobjat((0,0,171), SCREEN_SIZE, delta1x=-5,delta2x=-5,delta1y=5,delta2y=5)
                Randomize(bank_click).randleft()
                sleep(6.5)
            except:
                print("where is the bank?")
            return 0
        elif center == pos_2:
            STUCK_STATE = pos_4
            #pg.displayMousePosition()
            Randomize((271,281,74,84)).randleft() #tab2 in bank
            sleep(.3)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.3)
            Randomize((861,869,634,641)).randleft() #slot 2 in invo
            sleep(.3)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.3)
            Randomize((861,869,634,641)).randleft() #slot 2 in invo
            sleep(.3)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.3)
            Randomize((597,607,34,44)).randleft() # exit bank button
            sleep(.3)
            return 1
        elif center == pos_3:
            sleep(.3)
            STUCK_STATE = pos_4
            try:
                trapdoor_click = findobjat((125,0,207), delta1x=0,delta2x=0,delta1y=5,delta2y=6)
                Randomize(trapdoor_click).randleft()
                sleep(7)
            except:
                print("Where is the trapdoor...")
            return 0
        elif center == pos_4:
            STUCK_STATE = pos_4
            #pg.displayMousePosition()
            try:
                secret_door_click = findobjat((13,13,255), SCREEN_SIZE, delta1x=2,delta2x=2,delta1y=3,delta2y=3)
                Randomize(secret_door_click).randleft()
                sleep(5.8)
            except:
                print("IM STUCK AHHHHHH!")
            return 0
        elif center == pos_5:
            STUCK_STATE == pos_5
            Randomize((594,612,640,653)).randleft()
            sleep(8.5)
            try:
                cave_click = findobjat((0,107,44), SCREEN_SIZE, delta1x=0,delta2x=0,delta1y=0,delta2y=0)
                Randomize(cave_click).randleft()
                sleep(4)
            except:
                print("whyyyyyyyyyyyyyyyyyyyyyy")
            return 0
        elif center == pos_6:
            STUCK_STATE=pos_4
            Randomize((532,534,433,441)).randleft()
            sleep(3.6)
            return 0
        elif center == pos_7:
            STUCK_STATE=pos_4
            Randomize((640,644,391,397)).randleft()
            sleep(6.3)
            return 0
        elif center == pos_8:
            STUCK_STATE = pos_4
            Randomize((440,446,463,468)).randleft()
            sleep(3.2)
            Randomize((858,868,635,640)).randleft()#second bag slot
            sleep(.2)
            Randomize((483,491,464,471)).randleft()
            sleep(.2)
            Randomize((858,868,635,640)).randleft()#second bag slot
            sleep(.2)
            Randomize((483,491,464,471)).randleft()
            sleep(.2)
            Randomize((818,826,633,639)).randleft()#first bag slot
            sleep(5.2)
            return 0
        elif center == pos_9:
            STUCK_STATE = pos_4
            Randomize((480,486,437,440)).randleft()
            sleep(2.6)
            Randomize((428,430,428,434)).randleft()
            sleep(6.3)
            return 0
        else:
            try:
                secret_door_click = findobjat((13,13,255), SCREEN_SIZE, delta1x=2,delta2x=2,delta1y=3,delta2y=3)
                Randomize(secret_door_click).randleft()
                sleep(5.8)
            except:
                print("IM STUCK AHHHHHH!")
            return 0

    if STUCK_STATE == pos_5:
        if center == pos_6:
            STUCK_STATE=pos_4
            Randomize((532,534,433,441)).randleft()
            sleep(3.6)
            return 0
        else:
            STUCK_STATE = pos_5
            try:
                cave_click = findobjat((0,107,44), SCREEN_SIZE, delta1x=0,delta2x=0,delta1y=5,delta2y=5)
                Randomize(cave_click).randleft()
                sleep(5)
            except:
                print("whyyyyyyyyyyyyyyyyyyyyyy")
            return 0
count = 79
 
while True:
    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
        show_exit_popup()
        sys.exit(0)  # Exit the script when ESC is pressed
        break
    if count == 80:
        world_hopper()
        count = 0
    count = count + main()
    