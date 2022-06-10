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

f = open("file1.csv", "w")
f.truncate()
f.close()

#filename = "Test Audio/16-122828-0002.wav"

def toText(filename):
    r = sr.Recognizer()

    # open file
    with sr.AudioFile(filename) as source:

        # load audio to memory
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        

    print('#' * 80)
    print("Converted text:")
    print(text)
    print('#' * 80)

    with open ("file1.csv","w",encoding='UTF8') as file:    
        writer = csv.writer(file)
        writer.writerow(['command'])
        writer.writerow([text])
     
