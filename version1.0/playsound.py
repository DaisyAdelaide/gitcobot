#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3, time 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'English-UK')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()