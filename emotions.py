import speech_recognition as sr
import pandas as pd
import csv
import numpy
import gpiozero
import time
from guizero import App,Picture, PushButton

testing = []
actions = []

led1 = gpiozero.LED(6)
led2 = gpiozero.LED(13)
led3 = gpiozero.LED(19)
led4 = gpiozero.LED(26)


f = open("file2.csv", "w")
f.truncate()
f.close()



def listen1():
    with sr.Microphone(device_index = 1) as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)
        print("got it")
    return audio


def voice(audio1):
    r = sr.Recognizer()
    text1 = r.recognize_google(audio1)
    print ("you said: " + text1)
    with open ("file1.csv","w",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(['command'])
        writer.writerow([text1])


def write_file_2():
    data1 = ['command','response']
    data2 = ['turn on yellow', 'i like yellow']
    data3 = ['turn on red', 'you said red!']
    data4 = ['turn on blue','blue is my favourite']
    data5 = ['turn on green','green is nice']
    
    with open('file2.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data1)
        writer.writerow(data2)
        writer.writerow(data3)
        writer.writerow(data4)
        writer.writerow(data5)
        

def print_reply(testing,actions,axis=1):
    index = 0
    for command in testing.command:
        for action in actions.command:
            print('*')
            if command == action:
                print(actions.response[index])
                if index == 0:
                    led1.on()
                    time.sleep(2)
                if index == 1:
                    led2.on()
                    time.sleep(2)
                if index == 2:
                    led3.on()
                    picture = Picture(app, image = 'blue.png')
                    time.sleep(2)
                if index == 3:
                    led4.on()
                    time.sleep(2)
                    
                
            index = index + 1
        index = 0

def run():

    audio = listen1()

    voice(audio)

    write_file_2()

    testing = pd.read_csv('file1.csv')
    actions = pd.read_csv('file2.csv')

    print_reply(testing,actions)
    
    
app = App(title = 'Cobot')
picture = Picture(app, image = 'black.png')
button = PushButton(app, command = run)


app.display()
