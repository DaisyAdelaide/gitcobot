import pygame
import sys
import RPi.GPIO as GPIO
                        
def define():
    global one, two, three, four, five, six, seven, eight, smile
    one = pygame.image.load('1.JPG').convert_alpha()
    one = pygame.transform.scale(one,(548,380))
    two = pygame.image.load('2.JPG').convert_alpha()
    two = pygame.transform.scale(two,(548,380))
    three = pygame.image.load('3.JPG').convert_alpha()
    three = pygame.transform.scale(three,(548,380))
    four = pygame.image.load('4.JPG').convert_alpha()
    four = pygame.transform.scale(four,(548,380))
    five = pygame.image.load('5.JPG').convert_alpha()
    five = pygame.transform.scale(five,(548,380))
    six = pygame.image.load('6.JPG').convert_alpha()
    six = pygame.transform.scale(six,(548,380))
    seven = pygame.image.load('7.JPG').convert_alpha()
    seven = pygame.transform.scale(seven,(548,380))
    eight = pygame.image.load('8.JPG').convert_alpha()
    eight = pygame.transform.scale(eight,(548,380))
    smile = pygame.image.load('smile.JPG').convert_alpha()
    smile = pygame.transform.scale(smile,(217, 150))

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

button = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

pygame.init()
screen = pygame.display.set_mode((800,480),pygame.FULLSCREEN)

color = (255, 255, 255)

clock = pygame.time.Clock()

define()

blinking = [one,two,three,four,five,six,seven,eight]
index = 0
blink = 0
seconds = 0

gui_font = pygame.font.Font(None,30)

player_surf = blinking[index]

while True:

    if GPIO.input(button) == 1:
        print('Bop')
        pygame.quit()
        sys.exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    if seconds < 14:
        blink_func()
    
    screen.fill(color)
    screen.blit(smile, (286,300))
    screen.blit(player_surf, (126,0))

    pygame.display.update()
    clock.tick(20)
    seconds += 1

    if seconds == 60:
        seconds = 0 
      