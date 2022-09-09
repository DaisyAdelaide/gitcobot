#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
for v in voiceFemales:
    engine.setProperty('voice', v.id)
    engine.say('Hello world from ' + v.name)
    engine.runAndWait()