#hi there testing git
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

class Button:
    def __init__(self, text, width, height, pos):
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (0,120,70)
        self.text_surf = gui_font.render(text, 0,(210,255,50))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self):
        action = False
                        
        mouse_pos = pygame.mouse.get_pos()
        
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        pygame.draw.rect(screen,self.top_color, self.top_rect, 10)
        screen.blit(self.text_surf, self.text_rect)
        
        return action
                         
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

    while GPIO.input(button3) == 0:

        if GPIO.input(button4) == 1:
            pygame.quit()
            sys.exit()
                   
        black = (0, 0, 0)
        white = (255, 255, 255)
        orange = (255, 127, 39)
        font = pygame.font.Font('freesansbold.ttf', 20)
        #text = getText(start)

        if start == 0:
            text = 'Press blue to talk to me !'

        if GPIO.input(button2) == 1:
            print('pressed')
            text = functions.record()
            text = str(text)
            start = 1
    
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

##########
def maths_game():
    global seconds2, index, player_surf
    seconds2 = 30
    start = 0
    index = 0
    blinktime = 80
    player_surf = blinking[index]
    response = ''
    asked = 0
    problem = ''
    answer = ''
    sleep = 0

    while GPIO.input(button3) == 0:

        if GPIO.input(button4) == 1:
            pygame.quit()
            sys.exit()

        if GPIO.input(button) == 1 and start == 0:
            audio = functions.listen1()
            response = functions.voice(audio)
            response = str(response)
            start = 1
                   
        black = (0, 0, 0)
        white = (255, 255, 255)
        orange = (255, 127, 39)
        font = pygame.font.Font('freesansbold.ttf', 180)
        
        screen.fill(black)

        if asked == 0:
            problem, answer = sum()

        if start == 0:
            textSurface = font.render(problem, True, orange, black)
            textRect = textSurface.get_rect()
            textRect.center = (400, 200)
            asked = 1

        if start == 1:
            print(answer)
            print(response)
            if response == answer:
                textSurface = font.render('Right', True, orange, black)
                textRect = textSurface.get_rect()
                textRect.center = (400, 200)
                asked = 0
                start = 0
                sleep = 1

            elif response == 'I didnt catch that!':
                font = pygame.font.Font('freesansbold.ttf', 80)
                textSurface = font.render('I didnt catch that!', True, orange, black)
                textRect = textSurface.get_rect()
                textRect.center = (400, 200)
                start = 0
                sleep = 1

            elif response != answer:
                textSurface = font.render('Wrong', True, orange, black)
                textRect = textSurface.get_rect()
                textRect.center = (400, 200)
                start = 0
                sleep = 1

        #screen.fill(black)
        pygame.draw.rect(screen, black, pygame.Rect(400, 200, 200, 200))
        screen.blit(textSurface, textRect)
        pygame.display.update()
        clock.tick(20)

        pygame.display.update()
        clock.tick(20)
        if sleep == 1:
            time.sleep(2.5)
            sleep = 0

def sum():
    operands = ['+', '-', '/', '*']
    first_number = random.randint(0,10)
    second_number = random.randint(0,10)
    operand = random.choice(operands)

    problem = '{} {} {}'.format(first_number, operand, second_number)

    if operand == '+':
        answer = int(first_number) + int(second_number)

    if operand == '-':
        answer = int(first_number) - int(second_number)

    if operand == '*':
        answer = int(first_number) * int(second_number)

    if operand == '/':
        answer = int(first_number) / int(second_number)

    if (answer < 0) or (answer(type)==float):
        sum()

    return problem, str(answer)
####################################

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

gui_font = pygame.font.Font(None,30)

record_button = Button('Record', 100, 30, (0,0))
drive_button = Button('STOP', 100, 30, (620,200))
arm_button = Button('Arm', 100, 30, (620,300))

player_surf = blinking[index]

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
ser.flush()

f = open("SpeedData.csv", "w")
f.truncate()
f.close()

count = 0
blinktime2 = 80

line = ''

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('latin-1').rstrip()
        with open ("SpeedData.csv","a",encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow([line])
    
    if GPIO.input(button) == 1:
        print(count)
        count +=1
        chatbot()

    if GPIO.input(button4) == 1:
        pygame.quit()
        sys.exit()
##################################
    if GPIO.input(button2) == 1:
        maths_game()
###################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    if seconds < 14 :
        blink_func()

    if GPIO.input(button3) == 1:
        shrinkfunc()
        shrinking = 1

    if GPIO.input(button3) == 0 and shrinking == 1:
        player_surf = blinking[0]
        index = 0
        seconds = 50
        shrinking = 0
        mouth = smile
        blinktime2 = 80

    if GPIO.input(button2) == 1:
        player_surf = blinking[0]
        index = 0
        seconds = 50

    if line == 'Driving':
        shrinkfunc()
        shrinking = 11

    if line == 'Stop' and shrinking == 11:
        player_surf = blinking[0]
        index = 0
        seconds = 50
        shrinking = 0
        mouth = smile
        blinktime2 = 80

    screen.fill(orange)
    screen.blit(mouth, (286,300))
    screen.blit(player_surf, (126,0))

    pygame.display.update()
    clock.tick(20)
    seconds += 1

    if seconds == blinktime2:
        seconds = 0 
        blinktime2 = random.randint(35,100)
        
















