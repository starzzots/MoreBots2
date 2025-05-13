
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
pos1=(0,0,2)
pos2=(0,0,3)
pos3=(0,0,4)
pos4=(0,0,5)
pos5=(0,0,6)
pos6=(0,0,7)
pos7=(0,0,8)
fail1=(0,0,10)
fail2=(0,0,9)

token1c =(129,0,112) #(851,488)
token2c = (129,0,112) #(851,515)
token3c = (125,0,111) #(796,489)
token4c = (121,0,105) #(865,503)
token5c = (125,0,110) #(837,502)
token1calt = (128, 0, 111)
token4calt = (125,0,109) #(866,503)
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
    center=pg.pixel(823,479)
    if center == pos7:
        return 1
    else:
        return 0

def main():
    center=pg.pixel(823,479)
    token1=pg.pixel(851,488)#3rd building right side
    token2=pg.pixel(851,515)#4th building bottom side
    token3=pg.pixel(796,489)#1st building
    token4=pg.pixel(865,503)#4th building right most 
    token4alt=pg.pixel(866,503)#4th building right mosttoken 864,563
    token5=pg.pixel(837,502)#3rd building bottom side
    #print(center)
    if center == pos1:
        sleep(1.8)
        if token3 == token3c:
            Randomize((793,796,485,490)).uniclick()
            sleep(3)
            Randomize((798,815,532,549)).uniclick()
            sleep(3)
        else:
            Randomize((768,789,539,567)).uniclick()
            sleep(3)
    elif center == fail1:
        Randomize((838,844,195,200)).uniclick()
        sleep(3)
    elif center == fail2:
        Randomize((693,696,215,218)).uniclick()
        sleep(3)
    elif center == pos2:
        Randomize((833,837,606,615)).uniclick()
        sleep(4)
    elif center == pos3:
        sleep(2.5)
        if token1 == token1c or token1 == token1calt:
            Randomize((847,851,486,488)).uniclick()
            sleep(3.5)
            Randomize((819,833,416,437)).uniclick()
            sleep(5)
        elif token5 == token5c:
            Randomize((835,837,499,503)).uniclick()
            sleep(3.5)
            Randomize((835,848,407,419)).uniclick()
            sleep(5)
        else:
            Randomize((853,865,435,445)).uniclick()
            sleep(5)
    elif center == pos4:
        sleep(2.5)
        if token2 == token2c:
            Randomize((850,852,514,516)).uniclick()
            sleep(3)
            Randomize((846,857,408,423)).uniclick()
            sleep(4)
        elif token4 == token4c or token4alt == token4calt:
            Randomize((864,867,500,505)).uniclick()
            sleep(3)
            Randomize((835,843,423,432)).uniclick()
            sleep(4)
        else:
            Randomize((874,883,449,457)).uniclick()
            sleep(4)
    elif center == pos5:
        Randomize((873,878,388,399)).uniclick()
        sleep(4)
    elif center == pos6:
        Randomize((802,817,378,398)).uniclick()
        sleep(4)
    elif center == pos7:
        Randomize((462,465,462,463)).uniclick()
        sleep(4)
    
    sleep(1)
    return 0

if __name__ == "__main__":
    counter=0
    while True:
        sleep(1.5)
        counter=counter+logoutcounter()
        if counter >= 200:
            worldhopper()
            counter = 0
        else:
            
            main()