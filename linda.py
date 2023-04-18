import random
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import speech_recognition as sr
from pyChatGPT import ChatGPT
from chatgpt_wrapper import ChatGPT
import time
import webbrowser
import os
import pyjokes
import wikipedia
import arrays


# Speaking Method
def speak(text_to_speak):
    tts = gTTS(text_to_speak, slow=False, lang_check=True, lang="en",
               tld='us', pre_processor_funcs=[abbreviations, end_of_line])
    tts.save('audio.mp3')
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.set_volume(20)
    mixer.music.play()
    while mixer.music.get_busy():
        pass


def greeting():
    speak("Hello Sir. How Can I Help You Today ? ")

# Listening Method


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


def stopLinda():
    while True:
        stop = listen().lower()
        if "linda" in stop:
            speak("Ok Sir")
            mixer.stop()
            break

def WakeUp():
    bot = ChatGPT()
    speak("Initiating speech recognition")
    time.sleep(0.5)
    speak("Loading all systems")
    time.sleep(0.5)
    speak("All systems have been activated")
    time.sleep(0.5)
    speak("Now I am online")
    while True:
        myvoice = listen().lower()
        if "genius mode" in myvoice:
            speak("Activating Genius Mode")
            time.sleep(1)
            speak("Genius Mode Activated")
            while True:
                myvoice = listen().lower()
                if "exit genius mode" in myvoice:
                    speak("Deactivating Genius Mode")
                    time.sleep(1)
                    speak("Genius Mode Deactivated")
                    break
                elif myvoice in arrays.QUESTIONS:
                    response = bot.ask(myvoice)
                    speak("Please wait a moment")
                    speak(response)
        elif myvoice in arrays.GREETINGS:
            speak(random.choice(arrays.GREETINGS_RES))
        elif "time" in myvoice and "what" in myvoice:
            speak("The time is " + time.strftime("%I:%M %p") + " right now")
        elif "date" in myvoice and "what" in myvoice:
            speak("The date is " + time.strftime("%d/%m/%Y") + " right now")
        elif "shutdown speech recognition" in myvoice:
            speak("shutting down speech recognition")
            time.sleep(1)
            speak("Goodbye Sir")
            break
        elif "thank you" in myvoice:
            speak("You are welcome Sir")
        elif "how are you" in myvoice:
            speak(random.choice(arrays.HOWAREYOU))
        elif "what is your name" in myvoice:
            speak("My name is Linda, Sir")
        elif "who made you" in myvoice:
            speak("I was made by Mr. Abdallah Hussam")
        elif "search" in myvoice:
            speak("Searching" + myvoice.replace("search", ""))
            webbrowser.open("https://www.google.com/search?q=" + myvoice.replace("search for", ""))
            continue
        elif "joke" in myvoice:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "take screenshot" in myvoice or "take a screenshot" in myvoice or "capture the screen" in myvoice:
            speak("Alright sir, taking the screenshot")
            os.system("coreshot -f")

        elif "what do you know" in myvoice:
            speak("Linda knows a lot of things")
            time.sleep(1)
            speak("just a moment")
            result = wikipedia.summary(myvoice.replace(
                "what do you know about", ""), sentences=4)
            speak("According to wikipedia " + result)

        elif "shut down" in myvoice:
            speak("Shutting down")
            time.sleep(1)
            os.system("shutdown now")
            break

        elif "reboot" in myvoice or "restart" in myvoice:
            speak("Rebooting")
            time.sleep(1)
            os.system("reboot now")
            break

        elif "sleep" in myvoice:
           speak("Activating Sleep Mode")
           time.sleep(1)
           os.system("systemctl suspend")
           break
