import speech_recognition as sr
import pandas as pd
import csv
import numpy

testing = []
actions = []

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
    data2 = ['how are you', 'i am grand']
    data3 = ['what is your name', 'my name is cobot']
    data4 = ['hello','hi there']
    
    with open('file2.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data1)
        writer.writerow(data2)
        writer.writerow(data3)
        writer.writerow(data4)
        

def print_reply(testing,actions,axis=1):
    index = 0
    for command in testing.command:
        for action in actions.command:
            print('*')
            if command == action:
                print(actions.response[index])
            index = index + 1
        index =0

audio = listen1()

voice(audio)

write_file_2()

testing = pd.read_csv('file1.csv')
actions = pd.read_csv('file2.csv')

print_reply(testing,actions)
