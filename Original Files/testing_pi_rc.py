import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_ECHO = 26

GPIO.setup(GPIO_ECHO, GPIO.IN)

def read():
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300)/2
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = read()
            print(dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print('bye')
        GPIO.cleanup()
