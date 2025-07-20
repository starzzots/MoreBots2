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
#300 zoom

positions = [(0,0,1), (0,0,2), (0,0,3), (0,0,4),
             (0,0,5), (0,0,6), (0,0,7), (0,0,8),
             (0,0,9), (0,0,10), (0,0,11), (0,0,12),
             (0,0,13)]

rock_1_color = (0,0,200)
rock_2_color = (0,0,201)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#68,56


def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)

def logoutcounter():
    pass
    
def colors_match(obj_rgb_val1,obj_rgb_val2): #returns bool
    if obj_rgb_val1 == obj_rgb_val2:
        return True
    else:
        return False
    
def postion_is(center, n_pos_list):
    #takes center pos pixel color and a list of positions to track
    #keep it (0,0,n+1 sequence) color checks in sequence
    new_n = -1
    for i in range(len(n_pos_list)):
        if center == (0,0,i+1):
            new_n = i+1
            break
    return new_n

def state_is():
    bagslot_2_color_check = pg.pixel(865,637) #green, red or bag color
    bagslot_27_color_check = pg.pixel(909,853) 
    if bagslot_2_color_check == GREEN and bagslot_27_color_check == GREEN:
        return 1
    elif bagslot_2_color_check == GREEN:
        return 2
    elif bagslot_2_color_check == RED and bagslot_27_color_check == GREEN:
        return 3
    elif bagslot_2_color_check == RED and bagslot_27_color_check == BLUE:
        return 4
    elif bagslot_2_color_check == RED:
        return 5 
    elif bagslot_27_color_check == BLUE:
        return 6
    else:
        return 7
    
def chisel(n):
    for i in range(n):
        Randomize((945,952,849,857)).randleft()
        sleep(.05)
        Randomize((904,908,848,855)).randleft()
        sleep(.08)
        

def main():
    
    center = pg.pixel(503,466) # 300 zoom
    mining_color_check = pg.pixel(68,56)
    #empty_slot_color = (62,53,41)
    #charged_essence_color = (94, 86, 79)
    pos_number=postion_is(center, positions)
    state_number = state_is()

###################################################################

    if state_number == 1:
        sleep(.3)
        if pos_number == 1:
            Randomize((493,496,304,308)).randleft()
            sleep(12.3)
            Randomize((315,316,475,476)).randleft()
            sleep(1.6)
        elif pos_number == 2:
            Randomize((493,495,253,256)).randleft()
            sleep(12)
            Randomize((315,316,475,476)).randleft()
            sleep(1.6)
        elif pos_number == 3:
            Randomize((358,364,393,398)).randleft()
            sleep(7)
        else:
            pass
        #print("state 1")

###################################################################

    elif state_number == 2:
        sleep(.3)
        if pos_number == 1:
            if mining_color_check == GREEN:
                pass
            else:
                Randomize((514,527,539,550)).randleft()
                sleep(3)

        elif pos_number == 2:
            sleep(.3)
            if mining_color_check == GREEN:
                pass
            else:
                Randomize((511,524,392,398)).randleft()
                sleep(3)
        #print("state 2")

###################################################################

    elif state_number == 3:
        sleep(.3)
        if pos_number == 1:
            Randomize((492,496,303,309)).randleft()
            sleep(12)
            Randomize((315,316,475,476)).randleft()
            sleep(3)
        elif pos_number == 2:
            Randomize((493,495,253,256)).randleft()
            sleep(12)
            Randomize((315,316,473,474)).randleft()
            sleep(3)
        elif pos_number == 3:
            Randomize((358,365,392,398)).randleft()
            sleep(2.5)
        else:
            pass
        #print("state 3")

###################################################################  

    elif state_number == 4:
        sleep(.3)
        if pos_number == 4:
            Randomize((687,689,388,391)).randleft()
            sleep(3)
        elif pos_number == 5:
            Randomize((702,704,442,444)).randleft()
            sleep(3)
        elif pos_number == 6:
            Randomize((686,689,480,483)).randleft()
            sleep(3)
        elif pos_number == 10:
            Randomize((628,629,472,476)).randleft()
            sleep(3)
        elif pos_number == 11:
            Randomize((709,710,693,695)).randleft()
            sleep(3)
        elif pos_number == 12:
            Randomize((383,393,594,603)).randleft()
            sleep(3)
        else:
            pass
        #print("state 4")


###################################################################  
#   
    elif state_number == 5:
        sleep(.3)
        if pos_number == 4:
            Randomize((667,669,549,552)).randleft()
            sleep(3)
        elif pos_number == 3:
            Randomize((685,687,426,429)).randleft()
            sleep(3)
        elif pos_number == 5:
            Randomize((516,519,504,507)).randleft()
            sleep(5)
            Randomize((514,528,558,571)).randleft()
            sleep(3)

        elif pos_number == 1:
            if mining_color_check == GREEN:
                pass
            else:
                Randomize((514,527,539,550)).randleft()
                sleep(3)

        elif pos_number == 2:
            sleep(.3)
            if mining_color_check == GREEN:
                pass
            else:
                Randomize((511,524,392,398)).randleft()
                sleep(3)
        elif pos_number == 13:
            Randomize((487,493,478,482)).randleft()
            sleep(.2)

        else:
            pass
        #print("state 5")

###################################################################  
    
    elif state_number == 6: 
        sleep(.16)
        if pos_number == 4:
            chisel(26)
        elif pos_number == 13:
            chisel(24)
        else:
            pass
        #print("state 6")

###################################################################   

    elif state_number == 7:
        sleep(.3)
        if pos_number == 13:
            Randomize((577,579,378,382)).randleft()
            sleep(1.6)
        elif pos_number == 12:
            Randomize((367,369,319,320)).randleft()
            sleep(1.6)
        elif pos_number == 11:
            Randomize((380,381,459,462)).randleft()
            sleep(1.6)
        elif pos_number == 10:
            Randomize((339,343,581,583)).randleft()
            sleep(11)
            Randomize((389,391,517,521)).randleft()
            sleep(8.5)
            Randomize((517,529,560,575)).randleft()
            sleep(1.6)
        else:
            pass
    #print("state 7")
    
###################################################################

if __name__ == "__main__":
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
            show_exit_popup()
            sys.exit(0)  # Exit the script when ESC is pressed
            break
        else:
            sleep(.25)
            main()