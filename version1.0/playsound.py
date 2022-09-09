#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = engine.getProperty('voices') #get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[1].id)
engine.say('hi there my name is daisy')
for voice in voices:
	print(voice)
engine.runAndWait()