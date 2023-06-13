import pygame

pygame.init()

screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()

twister = pygame.image.load('twister.jpg').convert_alpha()
twister = pygame.transform.scale(twister,(480,480))

arrow = pygame.image.load('arrow.jpg').convert_alpha()
arrow = pygame.transform.scale(arrow,(480,480))

while True:

	screen.blit(twister,(160,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(20)

