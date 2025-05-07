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
#need to fix coords too tired will do another time

#200 zoom
pos1=(255,0,76)
pos2=(255,0,70)
pos3=(255,0,71)
pos4=(255,0,72)
pos5=(255,0,73)
pos6=(255,0,74)
pos7=(255,0,75)
fail1=(0,0,1)
fail2=(0,1,0)
tokenc=(255,0,0)


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
    center=pg.pixel(822,540)
    if center == pos1:
        return 1
    else:
        return 0
def main():
    tokenp=pg.pixel(838,539)
    center=pg.pixel(816,533)
    if center == pos1:
        Randomize((897,904,514,517)).randleft()
        sleep(1.5)
    elif fail1 == center:
        Randomize((928,933,731,738)).randleft()
        sleep(1.5)
    elif fail2 == center:
        Randomize((1133,1140,810,813)).randleft()
        sleep(1.5)
    elif center == pos2:
        Randomize((811,818,349,360)).randleft()
        sleep(1.5)
    elif center == pos3:
        Randomize((759,764,529,532)).randleft()
        sleep(3)
    elif center == pos4:
        if tokenc == tokenp:
            Randomize((835,841,530,532)).randleft()
            sleep(3)
        Randomize((771,779,531,544)).randleft()
        sleep(1.5)
    elif center == pos5:
        Randomize((820,825,602,614)).randleft()
        sleep(1.5)
    elif center == pos6:
        Randomize((864,870,666,673)).randleft()        
        sleep(1.5)
    elif center == pos7:
        Randomize((827,833,538,547)).randleft()
        sleep(1.5)
    
    return 0
counter=0
if __name__ == "__main__":
    while True:
        sleep(1.5)
        counter=counter+logoutcounter()
        if counter >= 200:
            worldhopper()
            counter = 0
        else:
            main()