import pygame
import csv 
#import RPi.GPIO as GPIO
import random

button = 17
button2 = 27
button3 = 22
button4 = 10

GPIO.setmode(GPIO.BCM)

#button = pink
#button2 = blue
#button3 = green
#button4 = Big Red button
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
screen = pygame.display.set_mode((800,480))

def load_animals():
    global animal_images
    dog = pygame.image.load('dog.png').convert_alpha()
    cat = pygame.image.load('cat.png').convert_alpha()
    snail = pygame.image.load('snail.png').convert_alpha()
    frog = pygame.image.load('frog.png').convert_alpha()
    lion = pygame.image.load('lion.png').convert_alpha()
    cow = pygame.image.load('cow.png').convert_alpha()
    fish = pygame.image.load('fish.png').convert_alpha()
    duck = pygame.image.load('duck.png').convert_alpha()
    sheep = pygame.image.load('sheep.png').convert_alpha()
    moose = pygame.image.load('moose.png').convert_alpha()
    Leprechaun  = pygame.image.load('lep.png').convert_alpha()

    animal_images = [cat, snail, dog, fish, duck, frog, lion, cow, sheep, moose, Leprechaun]

def maths_game():
    global end 
    #animals = ['cat','snail','dog', 'fish', 'duck', 'frog', 'lion', 'cow',  'sheep', 'moose','Leprechaun']
    animals = ['cat','snail','dog', 'fish', 'duck', 'frog', 'lion', 'cow',  'sheep', 'moose','Leprechaun']
    scores = [1,1,1,1,1,0,0,0,0,0,0]

    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 127, 39)
    blue = (25, 130, 196)
    yellow = (255, 202, 58)
    green = (138, 201, 38)
    red = (255, 51, 58)
    font = pygame.font.Font('freesansbold.ttf', 180)

    load_animals()

    problem, answer, points, first_number, second_number, operand = summ()
    
    right = 0
    ask = 0

    with open ("SpeechData.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow('')
        writer.writerow(['MATHS GAME BEGINNING'])
        writer.writerow('')
        writer.writerow('')
        writer.writerow([problem])

    #the exit button
    while GPIO.input(button3) == 0:

        #emergency exit
        #if GPIO.input(button4) == 1:
        #        pygame.quit()
        #        sys.exit()

        if ser.in_waiting > 0:
            line = ser.readline().decode('latin-1').rstrip()    

            if line == 'Speak':

                if operand == '+':
                    operand = 'plus'
                if operand == '-':
                    operand = 'minus'
                if operand == '*':
                    operand = 'multiplied by'
                if operand == '/':
                    operand = 'divided by'

                new_problem = '{} {} {}'.format(first_number, operand, second_number)

                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('rate', 125)
                engine.setProperty('voice', 'English-UK')
                opening = '   The question is : ' + new_problem
                engine.say(opening)
                engine.runAndWait()
                time.sleep(0.5)

                ask = 1

        screen.fill(blue)
        color_picked = blue
        font = pygame.font.Font('freesansbold.ttf', 180)
        textSurface = font.render(problem, True, yellow, blue)
        textRect = textSurface.get_rect()
        textRect.center = (400, 150)
        screen.blit(textSurface, textRect)

        #record maths answer
        if GPIO.input(button4) == 1 or ask == 1:
                ask = 0
                audio = functions.listen1()
                response = functions.voice(audio)
                response = str(response)
                original = response

                isolate = response.split(' ')
                isolate = str(isolate[-1])
                response = isolate
                
                if not response.isnumeric() and response != 'I didnt catch that!':
                    isolate = lev_distance.find_match(isolate)
                    response = str(w2n.word_to_num(isolate))     
                
                if response == answer:
                    screen.fill(green)
                    color_picked = green
                    font = pygame.font.Font('freesansbold.ttf', 100)
                    textSurface = font.render('Right', True, white, green)
                    textRect = textSurface.get_rect()
                    textRect.center = (400, 150)

                    textSurface2 = font.render('Points : {}'.format(points), True, orange, green)
                    textRect2 = textSurface2.get_rect()
                    textRect2.center = (400, 250)
                    screen.blit(textSurface2, textRect2)

                    correct_sound = mixer.Sound('correct.wav')
                    correct_sound.play()

                    right = 1

                elif response != answer:
                    screen.fill(red)
                    color_picked = red
                    textSurface = font.render('Wrong', True, white, red)
                    textRect = textSurface.get_rect()
                    textRect.center = (400, 150)
      
                    wrong_sound = mixer.Sound('wrong.wav')
                    wrong_sound.play()


                screen.blit(textSurface, textRect)
                pygame.display.update()
                time.sleep(2)

        if right == 1:
            right = 0
            select_character()
            audio = functions.listen1()
            character_chosen = functions.voice(audio)
            character_chosen = str(character_chosen)
            original1 = character_chosen

            x = 0

            if character_chosen == 'I didnt catch that!':
                wrong_sound = mixer.Sound('wrong.wav')
                wrong_sound.play()
                x = 1
            
            for animal in animals:
                if character_chosen == animal:
                    i = 0
                    for index in scores:
                        if character_chosen == animals[i]:
                            scores[i] += points 
                        i += 1
                    x = 1
            if x == 0:
                character_chosen = lev_animal.find_match(character_chosen)
                for animal in animals:
                    if character_chosen == animal:
                        i = 0
                        for index in scores:
                            if character_chosen == animals[i]:
                                scores[i] += points 
                            i += 1
            problem, answer, points, first_number, second_number, operand = summ()

            with open ("SpeechData.csv","a",encoding='UTF8') as file:
                    writer = csv.writer(file)
                    writer.writerow('')
                    writer.writerow([problem])
                    

            with open ("scores_data.csv","a",encoding='UTF8') as file:
                writer = csv.writer(file)
                writer.writerow('')
                to_write = 'maths answer given: ' + original
                writer.writerow([to_write])
                to_write = 'maths answer found: ' + response
                writer.writerow([to_write])
                to_write = 'character said: ' + original1
                writer.writerow([to_write])
                to_write = 'character chosen: ' + character_chosen
                writer.writerow([to_write])
                writer.writerow([scores])
                writer.writerow('')

        #load_animals()

        dict1 = {animal_images[i]:scores[i]for i in range(len(animal_images)) if scores[i]>0 }

        dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1)))

        list1 = list(dict1.keys())
        list1.reverse()

        x = 0
        if len(list1) > 0:
            for animal in list1:
                if x < 5:
                    lookup = animal
                    animal = pygame.transform.scale(animal,(130-x*15,130-x*15))
                    screen.blit(animal, (30 + x*135,350+x*15))
                    font = pygame.font.Font('freesansbold.ttf', 50)

                    textSurface3 = font.render('{}'.format(dict1[lookup]), True, white, blue)
                    textRect3 = textSurface3.get_rect()
                    textRect3.center = (30 + x*135,300+x*15)
                    screen.blit(textSurface3, textRect3)

                    x += 1


        pygame.display.update()
        clock.tick(10)

    end = time.time()

def select_character():
    character_sound = mixer.Sound('character.wav')
    character_sound.play()
    time.sleep(1)
    return 1

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def summ():
    operands = ['+', '-', '/', '*']
    answer = 0
    operand = ''
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    operand = random.choice(operands)
    points = 0

    problem = '{} {} {}'.format(first_number, operand, second_number)

    if operand == '+':
        answer = int(first_number) + int(second_number)
        points = 1

    if operand == '-':
        answer = int(first_number) - int(second_number)
        points = 2

    if operand == '*':
        answer = int(first_number) * int(second_number)
        points = 3

    if operand == '/':
        answer = (first_number) / (second_number)
        points = 4
        if (is_integer_num(answer)):
            return  problem, str(answer), points, first_number, second_number, operand 
        else:
            return(summ())

    if (answer < 0):
        return(summ())
    elif (answer > 60):
        return(summ())
    else:
        return problem, str(answer), points, first_number, second_number, operand


maths_game()