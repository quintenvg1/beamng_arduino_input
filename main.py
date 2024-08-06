import serial
import threading
import pyautogui
import time
blinkl_control = "l"
blinkr_control = "r"
handbrake_control = "space"
starter_control = "v"
_port='com4'
latest_input=""
myserial = serial.Serial(baudrate=9600, port=_port, timeout=0.1) #change port accordingly
pyautogui.FAILSAFE=False

def readinput():
    global latest_input
    while True:
        #print("reading input")
        latest_input = myserial.readline().decode('utf-8').strip()
        #print(latest_input)
        time.sleep(0.016)

#region controls

#left blinker
def blinkldwn():
    pyautogui.keyDown(blinkl_control)

def blinklup():
    pyautogui.keyUp(blinkl_control)

#right blinker
def blinkrdwn():
    pyautogui.keyDown(blinkl_control)

def blinkrup():
    pyautogui.keyUp(blinkl_control)

#handbrake
def hbup():
    pyautogui.keyDown(handbrake_control)

def hbdown():
    pyautogui.keyUp(handbrake_control)

#handbrake
def starterup():
    pyautogui.keyDown(starter_control)

def starterdown():
    pyautogui.keyUp(starter_control)

#endregion controls
def control():
    global latest_input
    while True:
        bits = latest_input.split(',')# become something like this 0,1,0,0 (blinkerl, blinkerr, handbrake, starter?)
        #control keyboard buttons.
        if(bits[0] == False):
            blinkldwn()
        else:
            blinklup()
        
        if(bits[1] == False):
            blinkrdwn()
        else:
            blinkrup()

        if(bits[2] == True):
            hbdown()
        else:
            hbup()

        if(bits[3] == False):
            starterdown()
        else:
            starterup()

def main():
    a = threading.Thread(target=readinput)#move reading input to a seperate thread.
    b = threading.Thread(target=control)
    a.start()
    b.start()
    print("started")
                 

main() #start the program, can only be interrupted with ctrl c.