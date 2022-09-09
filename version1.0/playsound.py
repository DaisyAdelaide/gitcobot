#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3, time 
engine = pyttsx3.init() 

voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('voice', voices[1].id)
engine.say("Hello I am the cobot") 
engine.runAndWait()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)