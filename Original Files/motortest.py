from gpiozero import Servo
from time import sleep

myGPIO = 5

servo = Servo(myGPIO)

servo.min()

