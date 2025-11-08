# storing the keystrokkes in the Text file

# file handeling - how to read, write and append to thr file
# r - reading
# w - writing
# a - appending 

# f = open("log.txt", 'r')
# fileData = f.read()
# print(fileData)

#listeners - listen to keystrokes
#use of the 'with' keyword - release memory/resousers automatically 

#using pynput
# controlling your mouse
#(left to right, top to bottom)
#from top-left of the screen you can imagine the top-left to be (0,0)
from pynput.mouse import Controller
def controlMouse():
    mouse= Controller()
    mouse.position =(10,20)
#controlMouse()

# listening to your mouse


# controlling your Keyboard
from pynput.keyboard import Controller
def controlKeyboard():
    keyboard = Controller()
    keyboard.type("im awsome")
#controlKeyboard()im awsome

# listening to your keyboard - will be finally used in the keylogger (what we need)
from pynput.keyboard import Listener
