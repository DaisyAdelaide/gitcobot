import pygame
import sys
import gpiozero

import functions

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
                         
def define():
    global one, two, three, four, five, six, seven, eight, smile
    one = pygame.image.load('1.JPG').convert_alpha()
    two = pygame.image.load('2.JPG').convert_alpha()
    three = pygame.image.load('3.JPG').convert_alpha()
    four = pygame.image.load('4.JPG').convert_alpha()
    five = pygame.image.load('5.JPG').convert_alpha()
    six = pygame.image.load('6.JPG').convert_alpha()
    seven = pygame.image.load('7.JPG').convert_alpha()
    eight = pygame.image.load('8.JPG').convert_alpha()
    smile = pygame.image.load('smile.JPG').convert_alpha()

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

gui_font = pygame.font.Font(None,30)

record_button = Button('Record', 200, 40, (720,200))
drive_button = Button('Drive', 200, 40, (720,400))
arm_button = Button('Arm', 200, 40, (720,600))

player_surf = blinking[index]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    if record_button.draw():
        functions.record()
        
    if drive_button.draw():
        functions.drive()
    
    if arm_button.draw():
        functions.arm()
    
    if seconds < 14:
        blink_func()

    screen.blit(smile, (0,300))
    screen.blit(player_surf, (0,0))

    pygame.display.update()
    clock.tick(20)
    seconds += 1

    if seconds == 80:
        seconds = 0 
        

