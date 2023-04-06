#! /usr/bin/python3

import pygame
import random
import gpiozero
#import RPi.GPIO as GPIO
#import functions
import time

#button3 = 22
#GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def define_image(image):
	global electronic_images
	image1 = image + '.png'
	image1 = pygame.image.load(image1).convert_alpha()
	image1 = pygame.transform.scale(image1,(100,100))

	electronic_images.append(image1)


def buttonColors():
	global button1Color, button2Color, button3Color
	button1Color = (0,191,255)
	button2Color = (30,144,255)
	button3Color = (65,105,225)

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

pygame.init()
screen = pygame.display.set_mode((800,480))
#screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
clock = pygame.time.Clock()

x = 0
picked = 0
question = 0

white = (255, 255, 255)
red = (255, 51, 58)
button1Color = (0,191,255)
button2Color = (30,144,255)
button3Color = (65,105,225)

buttonNumber = 0

electronic_images = []

global end, ts
end = 0 
ts = 0

font = pygame.font.Font('freesansbold.ttf', 100)
gui_font = pygame.font.Font(None,30)

electronics = ['Andorra',
				'Argentina', 
				'Armenia',
				'Afghanistan',
				'Australia',
				'Bolivia',
				'Brazil',
				'Belgium',
				'Canada', 
				'Cambodia',
				'China', 
				'Congo',
				'Cyprus',
				'Denmark',
				'Djibouti',
				'Equador',
				'Egypt',
				'Finland',
				'Figi',
				'France', 
				'Georgia',
				'Ghana',
				'Greece',
				'Haiti',
				'Hungary',
				'Honduras',
				'Iceland',
				'Iran',
				'Ireland', 
				'Italy',
				'India',
				'Japan',
				'Jordan',
				'Jamaica',
				'Kenya',
				'Kazakhstan',
				'Laos',
				'Liberia',
				'Madagascar',
				'Malta',
				'Mexico',
				'Malawi', 
				'Nigeria',
				'Nepal',
				'Oman',
				'Pakistan',
				'Portugal',
				'Panama',
				'Qatar',
				'Romania',
				'Rwanda',
				'Scotland',
				'Spain',
				'Syria',
				'Serbia',
				'Thailand',
				'Tanzania',
				'Uganda',
				'Uruguay',
				'Ukraine',
				'Venezuela',
				'Vietnam',
				'Vanuatu',
				'Yemen',
				'Zambia',
				'Zimbabwe'
				]


for element in electronics:
	image = element.lower()
	define_image(image)



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

	#if GPIO.input(button3) == 1:
	 #   pygame.quit()
	  #  sys.exit()

	if question == 0:
		countries = len(electronics)-1
		picked = random.randint(0,countries)
		numbers = [*range(0, countries+1, 1)]

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

