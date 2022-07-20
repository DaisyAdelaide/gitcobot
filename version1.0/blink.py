import pygame
import sys
import gpiozero
import serial
import pandas as pd
import csv 
import functions
import chat
import RPi.GPIO as GPIO

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
    global one, two, three, four, five, six, seven, eight, smile
    one = pygame.image.load('1.JPG').convert_alpha()
    one = pygame.transform.scale(one,(548,380))
    two = pygame.image.load('2.JPG').convert_alpha()
    two = pygame.transform.scale(two,(548,380))
    three = pygame.image.load('3.JPG').convert_alpha()
    three = pygame.transform.scale(three,(548,380))
    four = pygame.image.load('4.JPG').convert_alpha()
    four = pygame.transform.scale(four,(548,380))
    five = pygame.image.load('5.JPG').convert_alpha()
    five = pygame.transform.scale(five,(548,380))
    six = pygame.image.load('6.JPG').convert_alpha()
    six = pygame.transform.scale(six,(548,380))
    seven = pygame.image.load('7.JPG').convert_alpha()
    seven = pygame.transform.scale(seven,(548,380))
    eight = pygame.image.load('8.JPG').convert_alpha()
    eight = pygame.transform.scale(eight,(548,380))
    smile = pygame.image.load('smile.JPG').convert_alpha()
    smile = pygame.transform.scale(smile,(217, 150))

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
    start = 0

    while GPIO.input(button2) == 0:
                   
        black = (0, 0, 0)
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 20)
        #text = getText(start)

        if start == 0:
            text = 'Press green to talk to me !'

        if GPIO.input(button3) == 1:
            print('pressed')
            text = functions.record()
            text = str(text)
            start = 1

        textSurface = font.render(text, True, white, black)
        textRect = textSurface.get_rect()
        textRect.center = (400, 450)
        
        #screen.fill(black)
        screen.blit(textSurface, textRect)
        pygame.display.update()
        clock.tick(20)

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

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

color = (255, 255, 255)

clock = pygame.time.Clock()

define()

blinking = [one,two,three,four,five,six,seven,eight]
index = 0
blink = 0
seconds = 0

gui_font = pygame.font.Font(None,30)

record_button = Button('Record', 100, 30, (0,0))
drive_button = Button('STOP', 100, 30, (620,200))
arm_button = Button('Arm', 100, 30, (620,300))

player_surf = blinking[index]

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flush()

f = open("SpeedData.csv", "w")
f.truncate()
f.close()

count = 0
global stage
stage = 0

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        with open ("SpeedData.csv","a",encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow([line])
    
    if GPIO.input(button) == 1:
        print(count)
        count +=1
        chatbot()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
#    if record_button.draw():
#        functions.record()
        
#    if drive_button.draw():
#        functions.drive()
    
#    if arm_button.draw():
#        functions.arm()
    
    if seconds < 14:
        blink_func()
    
    screen.fill(color)
    screen.blit(smile, (286,300))
    screen.blit(player_surf, (126,0))

    pygame.display.update()
    clock.tick(20)
    seconds += 1

    if seconds == 80:
        seconds = 0 
        

