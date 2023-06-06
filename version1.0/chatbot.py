#! /usr/bin/python3
import pygame
import csv 
#import RPi.GPIO as GPIO
import random

import pygame
import sys
import gpiozero
import serial
import pandas as pd
import csv 
import functions
import RPi.GPIO as GPIO
import random
import time
import lev_distance
import lev_animal
from word2number import w2n
from pygame import mixer
from collections import OrderedDict
import operator
import pyttsx3, time 

def define():
    global one, two, three, four, five, six, seven, eight, smile, shock, mouth
    global shrink, shrink1, shrink2, shrink3, shrink4

    one = pygame.image.load('1O.jpg').convert_alpha()
    one = pygame.transform.scale(one,(548,380))
    two = pygame.image.load('2O.jpg').convert_alpha()
    two = pygame.transform.scale(two,(548,380))
    three = pygame.image.load('3O.jpg').convert_alpha()
    three = pygame.transform.scale(three,(548,380))
    four = pygame.image.load('4O.jpg').convert_alpha()
    four = pygame.transform.scale(four,(548,380))
    five = pygame.image.load('5O.jpg').convert_alpha()
    five = pygame.transform.scale(five,(548,380))
    six = pygame.image.load('6O.jpg').convert_alpha()
    six = pygame.transform.scale(six,(548,380))
    seven = pygame.image.load('7O.jpg').convert_alpha()
    seven = pygame.transform.scale(seven,(548,380))
    eight = pygame.image.load('8O.jpg').convert_alpha()
    eight = pygame.transform.scale(eight,(548,380))
    smile = pygame.image.load('smileO.jpg').convert_alpha()
    smile = pygame.transform.scale(smile,(217, 150))
    shrink1 = pygame.image.load('shrink1.jpg').convert_alpha()
    shrink1 = pygame.transform.scale(shrink1,(548,380))
    shrink2 = pygame.image.load('shrink2.jpg').convert_alpha()
    shrink2 = pygame.transform.scale(shrink2,(548,380))
    shrink3 = pygame.image.load('shrink3.jpg').convert_alpha()
    shrink3 = pygame.transform.scale(shrink3,(548,380))
    shrink4 = pygame.image.load('shrink4.jpg').convert_alpha()
    shrink4 = pygame.transform.scale(shrink4,(548,380))
    shock = pygame.image.load('OO.jpg').convert_alpha()
    shock = pygame.transform.scale(shock,(217, 150))

def shrinkfunc():
    global player_surf, shrink_index, shrink_blink, mouth

    mouth = shock

    if shrink_index < 3 and shrink_blink == 0:
        shrink_index += 1

    if shrink_index > 0 and shrink_blink ==1:
        shrink_index -= 1

    if shrink_index == 0:
        shrink_blink = 0

    if shrink_index == 3:
        shrink_blink = 1

    player_surf = shrink[shrink_index]

def blink_func():
    global player_surf, index, blink

    if index < 7 and blink == 0:
        index += 1

    if index > 0 and blink ==1:
        index -= 1

    if index == 0:
        blink = 0

    if index == 7:
        blink = 1

    player_surf = blinking[index]

def chatbot():
    global seconds2, index, player_surf
    seconds2 = 30
    start = 0
    index = 0
    blinktime = 80
    player_surf = blinking[index]
    global end 

    with open ("SpeechData.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['CHAT BOT BEGINNING'])
        writer.writerow('')

    while GPIO.input(button3) == 0:

       # if GPIO.input(button3) == 1:
        #    pygame.quit()
         #   sys.exit()
                   
        black = (0, 0, 0)
        white = (255, 255, 255)
        orange = (255, 127, 39)
        font = pygame.font.Font('freesansbold.ttf', 20)
        #text = getText(start)

        if ser.in_waiting > 0:
            line = ser.readline().decode('latin-1').rstrip()    

            if line == 'Speakkk':
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('rate', 125)
                engine.setProperty('voice', 'English-UK')
                opening = '  Hello there how are you ?'
                engine.say(opening)
                engine.runAndWait()
                time.sleep(0.5)

            if line == 'Speak':
                simon_says = ['move forward','turn green','turn yellow', 'move backwards', 'Turn Around', 'do a dance', 'Jump !']
                action = random.randint(1,3)
                pick = random.randint(0,6)
                if action % 2 == 0:
                    say = '     ' + simon_says[pick]
                else:
                    say = '     Simon Says ' + simon_says[pick]

                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('rate', 100)
                engine.setProperty('voice', 'English-UK')
                opening = sayomg !!
                engine.say(opening)
                engine.runAndWait()

            if line =='Speakkk':
                say = 'Welcome to Zen Maker Lab'
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('rate', 100)
                engine.setProperty('voice', 'English-UK')
                opening = say
                engine.say(opening)
                engine.runAndWait()

        if start == 0:
            text = 'Press record to talk to me !'

        if GPIO.input(button4) == 1:
            print('pressed')
            text = functions.record()
            text = str(text)
            start = 1
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('rate', 125)
            engine.setProperty('voice', 'English-UK')
            new_text = '   ' + text 
            engine.say(new_text)
            engine.runAndWait()
    
        if seconds2 < 14:
            blink_func()
        
        screen.fill(orange)
        screen.blit(mouth, (286,300))
        screen.blit(player_surf, (126,0))

        textSurface = font.render(text, True, white, orange)
        textRect = textSurface.get_rect()
        textRect.center = (400, 450)
        
        #screen.fill(black)
        pygame.draw.rect(screen, orange, pygame.Rect(0, 440, 800, 200))
        screen.blit(textSurface, textRect)
        pygame.display.update()
        clock.tick(20)

        seconds2 += 1

        if seconds2 == blinktime:
            seconds2 = 0 
            blinktime = random.randint(35,100)

    
    end = time.time()
    pygame.quit()
    sys.exit()

def getText(start):
    if start == 0:
        text = 'Press green to talk to me !'
        return text 

    if GPIO.input(button3) == 1:
        print('pressed')
        text = functions.record()
        text = str(text)
        start = 1
        return text


button = 17
button2 = 27
button3 = 22
button4 = 10

GPIO.setmode(GPIO.BCM)

#button = pink
#button2 = blue
#button3 = green
#button4 = Big Red button
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

color = (255, 255, 255)
orange = (255, 127, 39)

clock = pygame.time.Clock()

define()

mouth = smile
blinking = [one,two,three,four,five,six,seven,eight]
shrink = [shrink1, shrink2, shrink3, shrink4]
shrink_blink = 0
index = 0
blink = 0
shrink_index = 0
seconds = 0
seconds2 = 0
shrinking = 0
end = 0

driving_index = 0

gui_font = pygame.font.Font(None,30)

player_surf = blinking[index]


try:
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
except:
    try:
        ser = serial.Serial("/dev/ttyACM1", 115200, timeout=1)
    except:
        try:
            ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
        except:
            ser = 0


ser.flush()

#f = open("SpeedData.csv", "w")
#f.truncate()
#f.close()

count = 0
blinktime2 = 80

line = ''

while True:
	while GPIO.input(button3) == 0:
		chatbot()