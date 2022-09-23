import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
import matplotlib.pyplot as plt
import pigpio
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(12, GPIO.IN)
x = []
y = []
x_times = []
times = []

start = 0
end = 0
loop = 0

pi = pigpio.pi()

index = 0
started = 0

while (index < 7000): # Run forever
    if GPIO.input(12) == GPIO.HIGH:
        if started == 0:
            started = 1
            index = 0
        x.append(index)
        y.append(1)

    else:
        if started > 0:
            x.append(index)
            y.append(0)
            loop = 0
    
    #sleep(0.0001)
    index += 1



plt.plot(x,y)
plt.show()

#print(x,y,times)





pi.stop()
    