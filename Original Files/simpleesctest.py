from time import sleep
import pigpio
import RPi.GPIO as GPIO

pi = pigpio.pi()


ESC_GPIO = 4
ESC_GPIO2 = 3

print('start')


def arm():
    pi.set_servo_pulsewidth(ESC_GPIO2, 2200)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO2, 900)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO2, 500)
    sleep(2)

    print('one armed')

    pi.set_servo_pulsewidth(ESC_GPIO, 2200)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO, 900)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO, 500)
    sleep(2)

    print('two armed')




speed = 1100
pi.set_servo_pulsewidth(ESC_GPIO, speed)
pi.set_servo_pulsewidth(ESC_GPIO2, speed)
sleep(10)
pi.set_servo_pulsewidth(ESC_GPIO, 500)
pi.set_servo_pulsewidth(ESC_GPIO2, 500)


















