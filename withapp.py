import speech_recognition as sr
import pandas as pd
import csv
import numpy
import gpiozero
import time

import tkinter.messagebox
from tkinter import *

testing = []
actions = []

led1 = gpiozero.LED(6)
led2 = gpiozero.LED(13)
led3 = gpiozero.LED(19)
led4 = gpiozero.LED(26)

f = open("file1.csv", "w")
f.truncate()
f.close()

f = open("file2.csv", "w")
f.truncate()
f.close()
   

def build_app():
    win = Tk()
    win.title('Cobot')
    win.geometry('500x200')
    
    btn=tkinter.Button(win, text = 'record',width=10,height=5, command=listen1)
    btn.place(x=0,y=10)
    
    btn.pack()
    
    win.mainloop()
    
def red():
    led2.on()
    time.sleep(2)


def listen1():
    with sr.Microphone(device_index = 1) as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    voice(audio)
    return audio


def voice(audio1):
    
    r = sr.Recognizer()
    text1 = r.recognize_google(audio1)
    print ("you said: " + text1)
    with open ("file1.csv","w",encoding='UTF8') as f:
        writer = csv.writer(f)   
        writer.writerow([text1])
        f.close()
        
    print_reply(testing,actions)


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
    
    with open('file1.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['command'])
        f.close()
    

def print_reply(testing,actions,axis=1):
    index = 0
    testing = pd.read_csv('file1.csv')
    actions = pd.read_csv('file2.csv')
    for command in testing.command:
        for action in actions.command:
            print('*')
            if command == action:
                print(actions.response[index])
                if index == 0:
                    led1.on()
                    time.sleep(2)
                if index == 1:
                    red()
                if index == 2:
                    led3.on()
                    time.sleep(2)
                if index == 3:
                    led4.on()
                    time.sleep(2)
                                    
            index = index + 1
        index = 0


    
    

write_file_2()
build_app()





