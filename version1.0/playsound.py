#pip3 install pyttsx3
#apt-get install alsa-utils
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('voice', 'english_rp')
text = 'hello how are you'
new_text = '   ' + text 
engine.say(new_text)
engine.runAndWait()