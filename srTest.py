###############################################################################
#   Speech recognition function to transcribe an audio file using Google Speech Recognition
#   Source:
#   https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
#
#   Modified script into a function to use with recording script
###############################################################################
import speech_recognition as sr
import csv
from csv import writer

filename = "test.wav"

def toText(filename):
    
    r = sr.Recognizer()
    audio_data = filename
    text = r.recognize_google(audio_data)
    print('#' * 80)
    print("Converted text:")
    print(text)
    print('#' * 80)

toText(filename)