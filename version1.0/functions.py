import speech_recognition as sr
import pandas as pd
import csv
import numpy
import gpiozero
import time
from guizero import App, Picture, PushButton, Text
from time import sleep
import pigpio
import os
import sendmessage
import getresponse
import google


testing = []
actions = []

led1 = gpiozero.LED(6)
led2 = gpiozero.LED(13)
led3 = gpiozero.LED(19)
led4 = gpiozero.LED(26)

ESC_GPIO = 4
#pi = pigpio.pi()

def arm():
    sendmessage.arm()
    
def listen1():
    mic = sr.Microphone(device_index = 2)
    with mic as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        led3.on()
        audio = r.record(source=mic, duration=3)
        led3.off()
    return audio    
    
def voice(audio1):
    r = sr.Recognizer()
    try:
        text1 = r.recognize_google(audio1, language = 'en-IE')
    except:
        text1 = 'I didnt catch that!'

    with open ("SpeechData.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([text1])
    
    #print ("you said: " + text1)
    heard = ("I heard... " + text1)

    return str(text1)
    
 
def write_file_2():
    data1 = ['command','response']
    data2 = ['how are you', 'I am grand']
    data3 = ['turn on red', 'you said red!']
    data4 = ['turn on blue','blue is my favourite']
    data5 = ['turn on Green','Green is nice']
    data6 = ['start driving','I drove!']
    
    with open('file2.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data1)
        writer.writerow(data2)
        writer.writerow(data3)
        writer.writerow(data4)
        writer.writerow(data5)
        writer.writerow(data6) 
    
def print_reply(testing,actions,axis=1):
    index = 0
    reply = 0
    for command in testing.command:
        for action in actions.command:
            print('*')
            if command == action:
                reply += 1
                return actions.response[index]
            
            if index == 2:
                print('repeat')
                return 'I do not know the answer' 

            index = index + 1                
        
        index = 0
    
def drive():
    sendmessage.stop()
    

def record():

    #write_file_2()
    
    audio = listen1()

    text123 = voice(audio)
    
    #testing = pd.read_csv('file1.csv')
    #actions = pd.read_csv('file2.csv')
    #answer = print_reply(testing,actions)
    answer = getresponse.get_response(text123)

    if answer == 'I didnt catch that, try again!':
        response = 'I didnt catch that, try again!'
    else:
        response = answer
#        response = 'I heard ' + text123 + ', ' + answer

    with open ("SpeechData.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([response])
        writer.writerow(' ')
    return(response)

def record_QUIZ():
    
    audio = listen1()

    text123 = voice(audio)
    
    answer = google.goooogle(text123)

    if answer == 'I didnt catch that, try again!':
        response = 'I didnt catch that, try again!'
    else:
        response = answer
#        response = 'I heard ' + text123 + ', ' + answer

    with open ("Quiz_Me_Data.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([response])
        writer.writerow(' ')
    return(response)

    
def initial():
    #for final product, when starting pi only once for use, dont need at the moment
    os.system('sudo pigpiod')

def light_blue():
    led3.on()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    