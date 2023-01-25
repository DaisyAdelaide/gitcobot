#! /usr/bin/python3

import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()

numbers = [*range(1,21,1)]
question = 0
picked =0

end = 0

font = pygame.font.Font('freesansbold.ttf', 100)
gui_font = pygame.font.Font(None,150)

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

button1Color = (4, 99, 7)

while True:

	buttonOne = Button('BINGO', 400, 200, (200,200), button1Color)

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
		picked = str(picked)

	textSurface = font.render(picked, True, (32,178,170), (152,251,152))
	print(numbers)
	textRect = textSurface.get_rect()
	textRect.center = (400, 100)

	screen.fill((152,251,152))
	screen.blit(textSurface, textRect)

	if buttonOne.draw():
		ts = time.time()
		if (ts - end) > 0.5:
			question = 0
			button1Color = (4, 99, 7)
			end = time.time()
	
	pygame.display.update()
	clock.tick(10)


