import speech_recognition as sr
import pyttsx3
import f
import noisereduce as nr

import pyaudio
import wave
import sys
import keyboard
from time import sleep
from threading import Thread
from scipy.io import wavfile

#Audio recording stuff
p = pyaudio.PyAudio()

recordingLoop = False

frames = None
stream = None
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100

engine = f.audioOutputInit()
firstClick = True

def firstClickHandler():
    p = pyaudio.PyAudio()
        
    global frames
    global chunk
    global format
    global channels
    global rate
    global stream

    frames = []
    stream = p.open(format = format,
            channels = channels,
            rate = rate,
            input = True,
            frames_per_buffer = chunk)

    while not keyboard.is_pressed('f12'):
        data = stream.read(chunk)
        frames.append(data)
        sleep(0.01)


def secondClickHandler():
    global frames
    global chunk
    global format
    global channels
    global rate
    global stream
    stream.stop_stream()
    stream.close()

    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    # load data
    #rate, data = wavfile.read("output.wav")
    # select section of data that is noise
   # print(len(data))
    #noisy_part = data[0:100000]
    # perform noise reduction
    #reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=False,)
    
    r = sr.Recognizer()
    AUDIO_FILE = ("output.wav") 
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)   

    try:
        text = r.recognize_google(audio,language="pl-PL")
        global engine
        f.sayText(engine,text)

    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
  
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

t = None

def clickHandler(e):
    global firstClick
    global t

    if firstClick:
        firstClick = False
        print('start')

        t = Thread(target = firstClickHandler)
        t.start()
    else:
        print('stop')

        t.join()

        secondClickHandler()
        firstClick = True
       
def main():
    keyboard.on_release_key('f12',clickHandler,suppress=True)
    while True: 
        #print('eeeee')
        pass

if __name__ == '__main__':
    main()
