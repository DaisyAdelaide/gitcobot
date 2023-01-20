#! /usr/bin/python3

import pygame
import gpiozero
import pandas as pd 
import csv
import functions
import RPi.GPIO as GPIO
import sys

button4 = 10
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
screen = pygame.display.set_mode((800,480))
#screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

clock = pygame.time.Clock()

background = pygame.image.load('quiz_me.jpg').convert_alpha()
background = pygame.transform.scale(background,(548,380))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	screen.blit(background, (126,0))
	pygame.display.update()
	clock.tick(20)
