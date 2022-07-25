#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3, time 
engine = pyttsx3.init() 
engine.say("Hello I am the cobot") 
engine.runAndWait()