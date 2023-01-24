#! /usr/bin/python3

import pygame
import random
import gpiozero
import RPi.GPIO as GPIO
import functions
import time

button3 = 22
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def load_symbols():
	global electronic_images
	dc = pygame.image.load('dc.png').convert_alpha()
	dc = pygame.transform.scale(dc,(100,100))
	ac = pygame.image.load('ac.png').convert_alpha()
	ac = pygame.transform.scale(ac,(100,100))
	resistor = pygame.image.load('resistor.png').convert_alpha()
	resistor = pygame.transform.scale(resistor,(100,100))
	inductor = pygame.image.load('inductor.png').convert_alpha()
	inductor = pygame.transform.scale(inductor,(100,100))
	battery = pygame.image.load('battery.png').convert_alpha()
	battery = pygame.transform.scale(battery,(100,100))
	wire = pygame.image.load('wire.png').convert_alpha()
	wire = pygame.transform.scale(wire,(100,100))
	switch = pygame.image.load('switch.png').convert_alpha()
	switch = pygame.transform.scale(switch,(100,100))
	led = pygame.image.load('led.png').convert_alpha()
	led = pygame.transform.scale(led,(100,100))

	electronic_images = [dc, ac, resistor, inductor, battery, wire, switch, led]


pygame.init()
#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
clock = pygame.time.Clock()

x = 0
picked = 0
question = 0

white = (255, 255, 255)
red = (255, 51, 58)
button1Color = (4, 99, 7)
button2Color = (106, 207, 101)
button3Color = (61, 236, 85)

global end, ts
end = 0 
ts = 0

font = pygame.font.Font('freesansbold.ttf', 100)
gui_font = pygame.font.Font(None,30)

electronics = ['DC source', 'AC source', 'Resistor', 'Inductor', 'Battery', 'Wire', 'Switch','LED']

buttonNumber = 0

def buttonColors():
	global button1Color, button2Color, button3Color
	button1Color = (4, 99, 7)
	button2Color = (106, 207, 101)
	button3Color = (61, 236, 85)

load_symbols()

class Button:
    def __init__(self, text, width, height, pos, color):
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = color
        self.text_surf = gui_font.render(text, 0,(210,255,100))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self):
        action = False
          
        mouse_pos = pygame.mouse.get_pos()
        
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        pygame.draw.rect(screen,self.top_color, self.top_rect, 16)
        screen.blit(self.text_surf, self.text_rect)
        
        return action

while True:

	buttonOne = Button('', 275, 480, (0,0), button1Color)
	buttonTwo = Button('', 250, 480, (275,0), button2Color)
	buttonThree = Button('',275, 480, (525, 0), button3Color)

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.quit()
	            sys.exit()

	if GPIO.input(button3) == 1:
	    pygame.quit()
	    sys.exit()

	if question == 0:
		picked = random.randint(0,7)
		numbers = [0,1,2,3,4,5,6,7]
		numbers.remove(picked)
		second = random.choice(numbers)
		numbers.remove(second)
		third = random.choice(numbers)
		question += 1
		all_choice = [picked, second, third]
		random.shuffle(all_choice)
		index = 0
		for element in all_choice:
			if element == picked:
				buttonNumber = index
			index += 1


	textSurface = font.render(electronics[picked], True, (32,178,170), (152,251,152))
	textRect = textSurface.get_rect()
	textRect.center = (400, 100)


	screen.fill((152,251,152))

	x = 150
	for element in all_choice:
		screen.blit(electronic_images[element], (0+x,250))
		x += 200

	if buttonOne.draw():
		ts = time.time()
		if (ts - end) > 1:
			if buttonNumber == 0:
				question = 0
				buttonColors()
				end = time.time()
			else:
				button1Color = (255,0,0)
	    
	if buttonTwo.draw():
		ts = time.time()
		if (ts - end) > 1:
		    if buttonNumber == 1:
		        question = 0
		        buttonColors()
		        end = time.time()
		    else:
		    	button2Color = (255,0,0)

	if buttonThree.draw():
		ts = time.time()
		if (ts - end) > 1:
		    if buttonNumber == 2:
		        question = 0
		        buttonColors()
		        end = time.time()
		    else:
		    	button3Color = (255,0,0)

	screen.blit(textSurface, textRect)
	pygame.display.update()
	clock.tick(10)

