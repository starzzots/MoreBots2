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
stuck_state = (0,2,0)
pos_1 = (255,250,0)
pos_2=(73,64,52)
pos_3=(0,1,0)
pos_4 = (0,2,0)
pos_5 = (25,3,0)
pos_6 = (0,4,0)
pos_7 = (0,5,0)



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
    stuck_state = pos_4
    center = pg.pixel(502,468)
    #pg.displayMousePosition()
    #print(center)
    if stuck_state == pos_4:
        if center == pos_1:
            stuck_state = pos_4
            try:
                bank_click = findobjat((0,0,171), SCREEN_SIZE, delta1x=-5,delta2x=-5,delta1y=3,delta2y=3)
                Randomize(bank_click).randleft()
                sleep(7)
            except:
                print("where is the bank?")
        elif center == pos_2:
            stuck_state = pos_4
            #pg.displayMousePosition()
            Randomize((271,281,74,84)).randleft() #tab2 in bank
            sleep(.8)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.7)
            Randomize((861,869,634,641)).randleft() #slot 2 in invo
            sleep(.8)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.7)
            Randomize((861,869,634,641)).randleft() #slot 2 in invo
            sleep(.8)
            Randomize((202,210,112,120)).randleft() # click essense in bank
            sleep(.7)
            Randomize((597,607,34,44)).randleft() # exit bank button
            sleep(.7)
        elif center == pos_3:
            stuck_state = pos_4
            try:
                trapdoor_click = findobjat((125,0,207), delta1x=0,delta2x=0,delta1y=5,delta2y=6)
                Randomize(trapdoor_click).randleft()
                sleep(7)
            except:
                print("Where is the trapdoor...")
        elif center == pos_4:
            stuck_state = pos_4
            #pg.displayMousePosition()
            try:
                secret_door_click = findobjat((13,13,255), SCREEN_SIZE, delta1x=0,delta2x=0,delta1y=0,delta2y=0)
                Randomize(secret_door_click).randleft()
                sleep(5.8)
            except:
                print("IM STUCK AHHHHHH!")
        elif center == pos_5:
            stuck_state == pos_5
            Randomize((594,612,640,653)).randleft()
            sleep(8)
        elif center == pos_6:
            stuck_state=pos_4
            Randomize((532,534,433,441)).randleft()
            sleep(3.6)
        elif center == pos_7:
            stuck_state=pos_4
            Randomize((640,644,391,397)).randleft()
            sleep(3.6)
    elif stuck_state == pos_5:
        if center == pos_6:
            stuck_state=pos_4
            Randomize((532,534,433,441)).randleft()
            sleep(3.6)
        try:
            cave_click = findobjat((0,107,44), SCREEN_SIZE, delta1x=0,delta2x=0,delta1y=0,delta2y=0)
            Randomize(cave_click).randleft()
            sleep(5)
        except:
            print("whyyyyyyyyyyyyyyyyyyyyyy")

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
    