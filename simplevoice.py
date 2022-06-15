from time import sleep
import pigpio
import RPi.GPIO as GPIO
import speech_recognition as sr


def listen1():
    with sr.Microphone(device_index = 1) as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)
        print("got it")
        voice(audio)
    return audio

def voice(audio1):
    r = sr.Recognizer()
    text1 = r.recognize_google(audio1)
    
    print ("you said: " + text1)
    
    if (text1 == 'start driving'):
        speed = 1050
        pi.set_servo_pulsewidth(ESC_GPIO, speed)
        sleep(5)
        pi.set_servo_pulsewidth(ESC_GPIO, 0)
        pi.stop()


pi = pigpio.pi()

ESC_GPIO = 4
print('start')

pi.set_servo_pulsewidth(ESC_GPIO, 2500)
sleep(4)
pi.set_servo_pulsewidth(ESC_GPIO, 900)
sleep(4)

pi.set_servo_pulsewidth(ESC_GPIO, 500)


print('ready')
sleep(2)
audio = listen1()
