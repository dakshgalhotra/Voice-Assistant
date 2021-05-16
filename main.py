import speech_recognition as sr
import webbrowser
from time import ctime
import playsound
import os
import random
from gtts import gTTS
import pywhatkit
import time

r = sr.Recognizer()

def record_auido(ask = False):
    with sr.Microphone() as source:
        if ask:
            chatbot_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            chatbot_speak('Sorry, I did not get that')
        except sr.RequestError:
            chatbot_speak('Sorry, my speech service is down')
        return voice_data

def chatbot_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if'what is your name' in voice_data:
        chatbot_speak('My name is Chatbot')
    if 'what time is it' in voice_data:
        chatbot_speak(ctime())
    if 'search' in voice_data:
        search = record_auido('what do you want me to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        chatbot_speak('Here is what I found for ' + search)
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        chatbot_speak('playing' + song)
        pywhatkit.playonyt(song)
    if 'bye' in voice_data:
        exit()

time.sleep(2)
chatbot_speak('how can I help you')
while 1:
    voice_data = record_auido()
    respond(voice_data)