import pygame
from sys import exit

def define():
	global one, two, three, four, five, six, seven, eight, smile
	one = pygame.image.load('1.jpg').convert_alpha()
	two = pygame.image.load('2.jpg').convert_alpha()
	three = pygame.image.load('3.jpg').convert_alpha()
	four = pygame.image.load('4.jpg').convert_alpha()
	five = pygame.image.load('5.jpg').convert_alpha()
	six = pygame.image.load('6.jpg').convert_alpha()
	seven = pygame.image.load('7.jpg').convert_alpha()
	eight = pygame.image.load('8.jpg').convert_alpha()
	smile = pygame.image.load('smile.jpg').convert_alpha()

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

pygame.init()
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

define()

blinking = [one,two,three,four,five,six,seven,eight]
index = 0
blink = 0
seconds = 0

player_surf = blinking[index]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
	
	if seconds < 14:			
		blink_func()

	screen.blit(smile, (0,300))
	screen.blit(player_surf, (0,0))


	pygame.display.update()
	clock.tick(20)
	seconds += 1

	if seconds == 80:
		seconds = 0 
	

