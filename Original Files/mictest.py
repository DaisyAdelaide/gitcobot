import speech_recognition as sr


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
    return text1
    


audio = listen1()
voice(audio)