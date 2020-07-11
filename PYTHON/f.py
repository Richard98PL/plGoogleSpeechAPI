import pyttsx3

def audioOutputInit():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[3].id)
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 150)
    return engine
    
def sayText(engine,text):
    print(text)    
    engine.say(text)
    engine.runAndWait()
    engine.stop()