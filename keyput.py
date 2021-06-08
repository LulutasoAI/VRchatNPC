import time
import pynput
from pynput.keyboard import Key, Controller
import random
import sys
keyboard = Controller()
run_mode = sys.argv[1]
run_mode = int(run_mode)
def pressrel(ky):
    keyboard.press(ky)
    time.sleep(0.2)  #0.4 optimal
    keyboard.release(ky)
def pressrel2(ky):
    keyboard.press(ky)
    time.sleep(0.1)  #0.4 optimal
    keyboard.release(ky)
prestodo = ["w","a","s","d","c","z","c","z"]
if run_mode == 1:
    print("run_mode1 is running")
    for a in range(0,100000):
        random.shuffle(prestodo)
        for b in prestodo:
            pressrel(b)
elif run_mode == 2:
    print("run_mode2 is running")
    while True:
        pressrel2("a")
        pressrel2("d")
