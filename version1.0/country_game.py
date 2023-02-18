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
	dc = pygame.image.load('france.jpg').convert_alpha()
	dc = pygame.transform.scale(dc,(100,100))
	ac = pygame.image.load('ireland.png').convert_alpha()
	ac = pygame.transform.scale(ac,(100,100))
	resistor = pygame.image.load('canada.jpg').convert_alpha()
	resistor = pygame.transform.scale(resistor,(100,100))
	inductor = pygame.image.load('china.png').convert_alpha()
	inductor = pygame.transform.scale(inductor,(100,100))
	battery = pygame.image.load('argentina.png').convert_alpha()
	battery = pygame.transform.scale(battery,(100,100))
	wire = pygame.image.load('mexico.png').convert_alpha()
	wire = pygame.transform.scale(wire,(100,100))
	switch = pygame.image.load('spain.png').convert_alpha()
	switch = pygame.transform.scale(switch,(100,100))
	led = pygame.image.load('andorra.png').convert_alpha()
	led = pygame.transform.scale(led,(100,100))
	diode = pygame.image.load('congo.png').convert_alpha()
	diode = pygame.transform.scale(diode,(100,100))
	ground = pygame.image.load('greece.png').convert_alpha()
	ground = pygame.transform.scale(ground,(100,100))
	volt = pygame.image.load('japan.png').convert_alpha()
	volt = pygame.transform.scale(volt,(100,100))
	amp = pygame.image.load('brazil.png').convert_alpha()
	amp = pygame.transform.scale(amp,(100,100))
	portugal = pygame.image.load('portugal.png').convert_alpha()
	portugal = pygame.transform.scale(portugal,(100,100))
	scotland = pygame.image.load('scotland.png').convert_alpha()
	scotland = pygame.transform.scale(scotland,(100,100))
	ukraine = pygame.image.load('ukraine.png').convert_alpha()
	ukraine = pygame.transform.scale(ukraine,(100,100))
	ven = pygame.image.load('ven.png').convert_alpha()
	ven = pygame.transform.scale(ven,(100,100))
	hungary = pygame.image.load('hungary.png').convert_alpha()
	hungary = pygame.transform.scale(hungary,(100,100))
	aus = pygame.image.load('aus.png').convert_alpha()
	aus = pygame.transform.scale(aus,(100,100))
	italy = pygame.image.load('italy.png').convert_alpha()
	italy = pygame.transform.scale(italy,(100,100))
	iceland = pygame.image.load('iceland.png').convert_alpha()
	iceland = pygame.transform.scale(iceland,(100,100))
	zambia = pygame.image.load('zambia.png').convert_alpha()
	zambia = pygame.transform.scale(zambia,(100,100))
	madagascar = pygame.image.load('madagascar.png').convert_alpha()
	madagascar = pygame.transform.scale(madagascar,(100,100))

	electronic_images = [dc, 
						ac, 
						resistor, 
						inductor, 
						battery, 
						wire, 
						switch, 
						led, 
						diode, 
						ground,
						volt,
						amp,
						portugal,
						scotland,
						ukraine,
						ven,
						hungary,
						aus,
						italy,
						iceland,
						zambia,
						madagascar]

pygame.init()
#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
clock = pygame.time.Clock()

x = 0
picked = 0
question = 0

white = (255, 255, 255)
red = (255, 51, 58)
button1Color = (0,191,255)
button2Color = (30,144,255)
button3Color = (65,105,225)

global end, ts
end = 0 
ts = 0

font = pygame.font.Font('freesansbold.ttf', 100)
gui_font = pygame.font.Font(None,30)

electronics = ['France', 
				'Ireland', 
				'Canada', 
				'China', 
				'Argentina', 
				'Mexico', 
				'Spain',
				'Andorra',
				'Congo',
				'Greece',
				'Japan',
				'Brazil',
				'Portugal',
				'Scotland',
				'Ukraine',
				'Venezuela',
				'Hungary',
				'Australia',
				'Italy',
				'Iceland',
				'Zambia',
				'madagascar'
				]

buttonNumber = 0

def buttonColors():
	global button1Color, button2Color, button3Color
	button1Color = (0,191,255)
	button2Color = (30,144,255)
	button3Color = (65,105,225)

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

	buttonOne = Button('', 250, 480, (15,0), button1Color)
	buttonTwo = Button('', 245, 480, (280,0), button2Color)
	buttonThree = Button('',250, 480, (540, 0), button3Color)

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
		picked = random.randint(0,21)
		numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
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


	textSurface = font.render(electronics[picked], True, (32,178,170),(173, 216, 230))
	textRect = textSurface.get_rect()
	textRect.center = (400, 100)


	screen.fill((173, 216, 230))

	x = 100
	for element in all_choice:
		screen.blit(electronic_images[element], (0+x,250))
		x += 250

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

