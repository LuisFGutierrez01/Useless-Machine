#Useless machine 1 script
#Made by LuisFGutierrez01

import RPi.GPIO as GPIO
from time import sleep
import sys

in1 = 24
in2 = 23

GPIO.setmode(GPIO.BCM) #this is the name of the pins on board, not pin#
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW) #intializes both to low 
GPIO.output(in2,GPIO.LOW)

print("\nMotor is set to run for 1/4 seconds.")
print("Commands:\n   f:forward\n   b:back\n   e:exit")

def move_forward():
    print("Moving forward.")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(0.25)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def move_backward():
    print("Moving backward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(0.25)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

#python switch case pre python 3.10
def commands(i):
    cases = {
        'f': move_forward,
        'b': move_backward
        }
    return cases[i]()


while(True):

    x = input("Waiting for input...:")
    try:
        commands(x)
    except:
        if x == "e":
            print("Program Exiting")
            GPIO.cleanup()
            break
        print("Error, input again.")

