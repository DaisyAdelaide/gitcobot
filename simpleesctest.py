from time import sleep
import pigpio
import RPi.GPIO as GPIO

pi = pigpio.pi()


ESC_GPIO = 4
print('start')

pi.set_servo_pulsewidth(ESC_GPIO, 2200)
sleep(4)
pi.set_servo_pulsewidth(ESC_GPIO, 900)
sleep(4)

print('ready')
sleep(4)
speed = 1050
pi.set_servo_pulsewidth(ESC_GPIO, speed)
sleep(5)

pi.set_servo_pulsewidth(ESC_GPIO, 0)
sleep(4)