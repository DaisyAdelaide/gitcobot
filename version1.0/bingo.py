#! /usr/bin/python3

import pygame
import random
import time
from pygame import mixer

pygame.init()

#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
clock = pygame.time.Clock()

numbers = [*range(1,21,1)]
question = 0
picked = 0
used = []

end = 0

colours = []

for num in range(0,19):
	red = random.randint(0,255)
	blue = random.randint(0,255)
	green = random.randint(0,255)
	new_colour = (red,blue,green)
	colours.append(new_colour)

font = pygame.font.Font('freesansbold.ttf', 100)
font2 = pygame.font.Font('freesansbold.ttf', 70)
gui_font = pygame.font.Font(None,120)

class Button:
    def __init__(self, text, width, height, pos, color):
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = color
        self.text_surf = gui_font.render(text, 0,(54,17,89))
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

button1Color = (138,43,226)

while True:

	buttonOne = Button('Bingo!', 380, 200, (200,200), button1Color)
	screen.fill((0,206,209))

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.quit()
	            sys.exit()

	if question == 0:
		picked = random.choice(numbers)
		numbers.remove(picked)
		question = 1
		used.append(picked)
		picked = str(picked)
		
	red = random.randint(0,255)
	blue = random.randint(0,255)
	green = random.randint(0,255)
	textSurface = font.render(picked, True, (red,blue,green), (0,206,209))
	textRect = textSurface.get_rect()
	textRect.center = (400, 100)

	x = 45
	y = 45
	index = 0
	used.sort(reverse=False)
	print(used)
	for element in used:
		textSurface1 = font2.render(str(used[index]), True, colours[index],(0,206,209))
		textRect1 = textSurface1.get_rect()
		textRect1.center = (x, y)
		x += 100
		if index % 2 != 0:
			y += 100
			if index > 10:
					x = 630
			else:
				x = 45
		if index == 9:
			x = 630
			y = 45
		index += 1
		screen.blit(textSurface1, textRect1)
	
	screen.blit(textSurface, textRect)

	if buttonOne.draw():
		ts = time.time()
		if (ts - end) > 0.5:
			wrong_sound = mixer.Sound('bingo.MP3')
			wrong_sound.play()
			time.sleep(2.3)
			wrong_sound.stop()
			question = 0
			end = time.time()

	pygame.display.update()
	clock.tick(10)


