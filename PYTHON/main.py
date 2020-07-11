import speech_recognition as sr
import pyttsx3
import f

r = sr.Recognizer()
mic = sr.Microphone()
engine = f.audioOutputInit()
while True :
    with mic as source:
        r.adjust_for_ambient_noise(source)
        f.sayText(engine,"Mów")
        captured_audio = r.record(source,duration=2)
        #captured_audio = r.listen(source)
        print('End')

        try:
            text = r.recognize_google(captured_audio,language="pl-PL")
            f.sayText(engine,text)
        
        except:
            print('Error')

