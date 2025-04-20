import sys
import psutil
import pyautogui as pg
from random import randint
from time import time

# Check OS for appropriate window control module
if sys.platform.startswith("win"):
    import pygetwindow as gw
elif sys.platform.startswith("darwin"):
    from AppKit import NSWorkspace
    from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGWindowListExcludeDesktopElements
elif sys.platform.startswith("linux"):
    import subprocess

def is_runelite_running():
    """Check if RuneLite is running."""
    for process in psutil.process_iter(attrs=["name"]):
        if "RuneLite" in process.info["name"]:
            return True
    return False

def get_runelite_window_size():
    """Get RuneLite's window position, width, and height (cross-platform)."""
    if sys.platform.startswith("win"):
        # Get RuneLite window (Windows)
        windows = gw.getWindowsWithTitle("RuneLite")
        if windows:
            win = windows[0]  # First matching window
            return win.left, win.top, win.width, win.height

    elif sys.platform.startswith("darwin"):
        # Get RuneLite window (Mac)
        options = kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements
        window_list = CGWindowListCopyWindowInfo(options, 0)
        
        for window in window_list:
            if "RuneLite" in window.get("kCGWindowName", ""):
                bounds = window.get("kCGWindowBounds", {})
                return bounds["X"], bounds["Y"], bounds["Width"], bounds["Height"]

    elif sys.platform.startswith("linux"):
        # Get RuneLite window (Linux)
        try:
            result = subprocess.run(["wmctrl", "-lG"], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            for line in lines:
                parts = line.split()
                if "RuneLite" in line:
                    x, y, width, height = map(int, parts[2:6])
                    return x, y, width, height
        except FileNotFoundError:
            print("wmctrl is not installed. Install it using: sudo apt install wmctrl")

    return None  # RuneLite not found or unable to get size
padding = 10 
# Example usage
if __name__ == "__main__":
    if is_runelite_running():
        size = get_runelite_window_size()
        if size:
            x, y, width, height = size
            pg.moveTo(x+padding,y+padding,.5)
            pg.moveTo(width+x-padding,height+y-padding,.5)
            print(f"RuneLite is open at ({x}, {y}) with size {width}x{height}")
        else:
            print("RuneLite is running but could not get window size.")
    else:
        print("RuneLite is not running.")
