from pynput.mouse import Controller
from pynput.keyboard import Controller

#(left to right, top to bottom)
#from top left of screen you can imagine the top left to be (0,0)
#you can't controller mouse and keyboard a same time

def controlMouse():
    mouse = Controller()
    mouse.position=(100, 2000)



def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am freaking good")

controlKeyboard()




    
#call the controlMouse function
#controlling your mouse
#listening to your mouse
#controlling your keyboard
#listening to your keyboard - will be finally used in our keyloggers
