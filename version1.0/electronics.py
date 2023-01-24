#! /usr/bin/python3

import pygame
import random

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

	electronic_images = [dc, ac, resistor, inductor]


pygame.init()
screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()

x = 0
picked = 0
question = 0

white = (255, 255, 255)
red = (255, 51, 58)

font = pygame.font.Font('freesansbold.ttf', 100)
gui_font = pygame.font.Font(None,30)

electronics = ['DC source', 'AC source', 'Resistor', 'Inductor']

load_symbols()

class Button:
    def __init__(self, text, width, height, pos):
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (100,120,100)
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

buttonOne = Button('', 200, 40, (200,400))
buttonTwo = Button('', 200, 40, (400,400))

while True:

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.quit()
	            sys.exit()

	if question == 0:
		picked = random.randint(0,3)
		numbers = [0,1,2,3]
		numbers.remove(picked)
		second = random.choice(numbers)
		numbers.remove(second)
		third = random.choice(numbers)
		question += 1
		all_choice = [picked, second, third]
		random.shuffle(all_choice)

	textSurface = font.render(electronics[picked], True, red, white)
	textRect = textSurface.get_rect()
	textRect.center = (400, 100)


	screen.fill((25, 130, 196))

	x = 150
	for element in all_choice:
		screen.blit(electronic_images[element], (0+x,250))
		x += 200

	if buttonOne.draw():
	    question = 0
	    
	if buttonTwo.draw():
	    question = 1

	screen.blit(textSurface, textRect)
	pygame.display.update()
	clock.tick(10)


	#this is working to display images, check notebook for next steps. 