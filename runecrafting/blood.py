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
    
from tools.clicks import *
from time import sleep
from tools.tools import *
import keyboard
#400 zoom I need to edit this potentially
#full screen 1920x1080
SCREEN_SIZE=(0,0,1920,1080)
STUCK = False # I need to fix the stuck feature

bank_screen = (73,64,52)
pos_1 = (0,1,0)
pos_2 = (0,2,0)
pos_3 = (25,3,0)
pos_4 = (0,4,0)
pos_5 = (0,5,0)
pos_6 = (0,6,0)
pos_8 = (0,8,0)
pos_9 = (255,250,0)
bank_color = (56,0,0)
trapdoor_color = (255,51,255)
wall_color = (50,87,255)
fifth_inventory_check = (62,53,41)
cave_cord_click = (1042,1044,905,908)
cave2_cord_click = (860,863,490,496)
mysterious_ruins_cords = (975,985,444,452)
blood_alter_cords = (752,763,524,530)
pure_essence_cords_bank = (518,532,136,142)
first_inventory_cords = (1455,1468,760,771)
second_inventory_cords = (1497,1508,759,771)
third_inventory_cords = (1542,1549,758,764)
forth_inventory_cords = (1583,1593,758,768)
exit_bank_button = (920,927,61,68)
start_bank_click = (589,598,96,106)
bonus_check_color = (56,255,255)
bonus_check_cord = (1587,768)
#potentially need to update the core loop in order to get the stuck feature to work
def bank_operation():
    Randomize(start_bank_click).randleft()
    sleep(1)
    Randomize(pure_essence_cords_bank).randleft()
    sleep(.8)
    Randomize(second_inventory_cords).randleft()
    sleep(.8)
    Randomize(pure_essence_cords_bank).randleft()
    sleep(.8)
    Randomize(second_inventory_cords).randleft()
    sleep(.8)
    Randomize(pure_essence_cords_bank).randleft()
    sleep(.8)
    Randomize(exit_bank_button).randleft()
    sleep(.8)
    
def move_to_bank():
    try:
        bank_cords = findobjat(bank_color,SCREEN_SIZE, delta1x=6, delta2x=8, delta1y=6, delta2y=8)
        Randomize(bank_cords).randleft()
        sleep(9)
    except:
        print("couldnt find bank")

def move_to_trapdoor():
    try:
        trapdoor_cords = findobjat(trapdoor_color,SCREEN_SIZE, delta1x=6, delta2x=8, delta1y=6, delta2y=8)
        Randomize(trapdoor_cords).randleft()
        sleep(12.8)
    except:
        print("couldnt find trapdoor")

def move_to_cave():
    Randomize(cave_cord_click).randleft()
    sleep(7)

def blood_alter_operations():
    Randomize(blood_alter_cords).randleft()
    sleep(3)
    Randomize(second_inventory_cords).randleft()
    sleep(.5)
    Randomize((801,807,526,530)).randleft()
    sleep(.5)
    Randomize(second_inventory_cords).randleft()
    sleep(.5)
    Randomize((801,807,526,530)).randleft()
    sleep(.5)
    Randomize(first_inventory_cords).randleft()
    sleep(5.5)

def house_operations():
    Randomize((801,803,494,496)).randleft()
    sleep(4)
    Randomize((740,742,490,492)).randleft()
    sleep(7)

def world_hopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presses
    sleep(7.5)
    keyboard.press('x')# bag hotkey press
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)
    

     
           
def main():
    center = pg.pixel(824,537)

    print(center)
    
    sleep(.5)
    if pg.pixel(bonus_check_cord[0],bonus_check_cord[1]) != bonus_check_color:
        Randomize(third_inventory_cords).randleft()
        sleep(.8)
        return 0
    
    elif center == bank_screen:
        bank_operation()
        return 1

    
    elif center == pos_9:
        move_to_bank()
        return 0

    
    elif center == pos_1:
        move_to_trapdoor()
       
        return 0

    
    elif center == pos_2:
        try:
            wall_cords = findobjat(wall_color,SCREEN_SIZE, delta1x=5, delta2x=8, delta1y=5, delta2y=8)
            Randomize(wall_cords).randleft()
            sleep(7)
            return 0
        except:
            print("couldnt find wall")
            return 0

    
    elif center == pos_3:
        Randomize(cave_cord_click).randleft()
        sleep(13.4)
        return 0

    elif center == pos_4:
        Randomize(cave2_cord_click).randleft()
        sleep(4)
        return 0
    
    elif center == pos_5:
        Randomize(mysterious_ruins_cords).randleft()
        sleep(6)
        return 0
    
    elif center == pos_6:
        blood_alter_operations()
        return 0 
    
    elif center == pos_8:
        house_operations()
        return 0 
        
    else:  
        print(center)
        try:
            wall_cords = findobjat(wall_color,SCREEN_SIZE, delta1x=4, delta2x=8, delta1y=4, delta2y=8)
            Randomize(wall_cords).randleft()
            sleep(5)
            return 0
        except:
            print("couldnt find wall")
            return 0
        
            
count = 0
 
while True:
    count = count + main()
    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
        show_exit_popup()
        sys.exit(0)  # Exit the script when ESC is pressed
        break
    if count == 80:
        world_hopper()
        count = 0
    
    
    