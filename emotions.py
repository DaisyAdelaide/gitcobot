import speech_recognition as sr
import pandas as pd
import csv
import numpy
import gpiozero
import time
from guizero import App, Picture, PushButton, Text
from time import sleep
import pigpio
import RPi.GPIO as GPIO
import os

testing = []
actions = []

led1 = gpiozero.LED(6)
led2 = gpiozero.LED(13)
led3 = gpiozero.LED(19)
led4 = gpiozero.LED(26)

f = open("file2.csv", "w")
f.truncate()
f.close()

ESC_GPIO = 4
pi = pigpio.pi()

def arm():
    pi.set_servo_pulsewidth(ESC_GPIO, 2200)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO, 900)
    sleep(4)
    pi.set_servo_pulsewidth(ESC_GPIO, 500)
    armbutton.hide()
    
def listen1():
    with sr.Microphone(device_index = 1) as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        led3.on()
        audio = r.listen(source)
        print("got it")
        led3.off()
    return audio

def voice(audio1):
    r = sr.Recognizer()
    text1 = r.recognize_google(audio1)
    print ("you said: " + text1)
    heard = ("I heard... " + text1)
    text = Text(app, text = heard, grid = [0,1])
    with open ("file1.csv","w",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['command'])
        writer.writerow([text1])

def write_file_2():
    data1 = ['command','response']
    data2 = ['turn on yellow', 'i like yellow']
    data3 = ['turn on red', 'you said red!']
    data4 = ['turn on blue','blue is my favourite']
    data5 = ['turn on Green','Green is nice']
    data6 = ['start driving','I drove!']
    
    with open('file2.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data1)
        writer.writerow(data2)
        writer.writerow(data3)
        writer.writerow(data4)
        writer.writerow(data5)
        writer.writerow(data6)
  
def print_reply(testing,actions,axis=1):
    index = 0
    reply = 0
    for command in testing.command:
        for action in actions.command:
            print('*')
            if command == action:
                reply += 1
                print(actions.response[index])
                text = Text(app, text = actions.response[index], grid = [0,2])
                if index == 0:
                    led1.on()
                    picture = Picture(app, image = 'yellowcheeks.gif',grid = [0,0])
                if index == 1:
                    led2.on()                    
                    picture = Picture(app, image = 'redbrows.gif',grid = [0,0])
                if index == 2:
                    led3.on()
                    picture = Picture(app, image = 'bluenose.gif',grid = [0,0])
                if index == 3:
                    led4.on()
                    picture = Picture(app, image = 'greeneyes.gif',grid = [0,0])
                if index == 4:
                    drive()
                            
            index = index + 1
        if reply == 0:
            text = Text(app, text = 'I don\'t know that phrase.', grid = [0,2])
            picture = Picture(app, image = 'confused.gif',grid = [0,0])
        
        index = 0
    
def drive():
    speed = 1100
    pi.set_servo_pulsewidth(ESC_GPIO, speed)
    sleep(15)
    pi.set_servo_pulsewidth(ESC_GPIO, 500)
    picture = Picture(app, image = 'happy.gif',grid = [0,0])    

def record():
    write_file_2()
    
    audio = listen1()
    voice(audio)
    
    testing = pd.read_csv('file1.csv')
    actions = pd.read_csv('file2.csv')
    print_reply(testing,actions)
    
def initial():
    #for final product, when starting pi only once for use
    os.system('sudo pigpiod')
    
app = App(title = 'Cobot', width = 850, height = 750, layout = 'grid')

picture = Picture(app, image = 'normal.gif', grid = [0,0])
record = PushButton(app, command = record, text = 'record', grid = [1,1])
drivebutton = PushButton(app, command = drive, text = 'drive', grid = [1,2])
armbutton = PushButton(app, command = arm, text = 'arm', grid = [1,3])
#buttonone = PushButton(app, command = initial, text = 'stepone', grid = [0,4])

app.display()
