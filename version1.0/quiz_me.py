#! /usr/bin/python3

import pygame
import gpiozero
import pandas as pd 
import csv
import functions
import google
import RPi.GPIO as GPIO
import sys
import pyttsx3, time 
from pygame import mixer

button4 = 10
button3 = 22
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
#screen = pygame.display.set_mode((800,480))
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

clock = pygame.time.Clock()

background = pygame.image.load('quiz_me.jpg').convert_alpha()
background = pygame.transform.scale(background,(800,480))

while True:
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

#blit - image, co-ordinates
	screen.blit(background, (0,0))
	pygame.display.update()
	clock.tick(20)

	with open ("Quiz_Me_Data.csv","a",encoding='UTF8') as file:
		writer = csv.writer(file)
		writer.writerow(['STARTING SESSION'])
		writer.writerow('')

	if GPIO.input(button4) == 1:
			print('pressed')
			text = functions.record_QUIZ()
			text = str(text)
			start = 1
			engine = pyttsx3.init()
			voices = engine.getProperty('voices')
			engine.setProperty('rate', 125)
			engine.setProperty('voice', 'English-UK')
			new_text = '   ' + text 
			engine.say(new_text)
			engine.runAndWait() 
 