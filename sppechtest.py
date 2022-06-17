import speech_recognition as sr
import pandas as pd
import csv
import gpiozero
led3 = gpiozero.LED(19)

def listen1():
    with sr.Microphone(device_index = 1) as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        led3.on()
        audio = r.listen(source)
        print("got it")
        led3.off()
    return audio

def voice(audio1):
    r = sr.Recognizer()
    text1 = ''
    text1 = r.recognize_google(audio1)
    print ("you said: " + text1)
    with open ("testing.csv","a",encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow([text1])
        file.close()
        
audio = listen1()
voice(audio)
audio = listen1()
voice(audio)
audio = listen1()
voice(audio)