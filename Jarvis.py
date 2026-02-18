import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import os
import musicLibrary
import requests
import difflib
import pywhatkit
from groq import Groq
import pygame
from gtts import gTTS

# 1. SETUP CLIENTS
recognizer = sr.Recognizer()
newsapi = "Paste your api here"

# Initialize Groq Client
client = Groq(
    api_key="Paste your api here"
)

# def old_speak(text):
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# def speak(text): if you want to run this make sure uncomment 23rd line and comment 24th line
#     tts = gTTS(text)
#     tts.save('temp.mp3')

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep program running until music stops
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

def processCommand(c): 
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
        
    elif "play music" in c.lower():
        speak("playing music for you")
        webbrowser.open("https://www.youtube.com/watch?v=bfW6dzCFy2A&list=RDbfW6dzCFy2A&start_radio=1")
        
    elif "close chrome" in c.lower():
        speak("Closing chrome")
        time.sleep(1)
        os.system("taskkill /im chrome.exe /f")

    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
        
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com/")
        
    elif "open leetcode" in c.lower():
        speak("Opening Leetcode")
        webbrowser.open("https://leetcode.com/")
        
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
        
    elif "show me the list of songs" in c.lower() or "list songs" in c.lower() or "available songs" in c.lower():
        speak("Here are the songs available in your music library")
        songs = list(musicLibrary.music.keys())
        print("\n--- Available Songs ---")
        for index, song in enumerate(songs, 1):
            print(f"{index}. {song}")
        print("-----------------------\n")
        
    elif c.lower().startswith("play "):
        song = c.lower().replace("play ", "", 1).strip()
        
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            available_songs = list(musicLibrary.music.keys())
            matches = difflib.get_close_matches(song, available_songs, n=1, cutoff=0.4)
            
            if matches:
                best_match = matches[0]
                speak(f"Playing {best_match}")
                webbrowser.open(musicLibrary.music[best_match])
            else:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)
            
    elif 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if not articles:
                speak("No news available right now")
                return
            for article in articles:
                speak(article['title'])
        else:
            speak("Failed to fetch news")
            
    else:
        # --- GROQ AI INTEGRATION ---
        # If the command is not found above, send it to Llama 3.3
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Answer concisely in 2-3 paragraphs: {c}", 
                    }
                ],
                model="llama-3.3-70b-versatile", 
            )
            
            response = chat_completion.choices[0].message.content
            print("\nJarvis says:", response)
            speak(response)

        except Exception as e:
            print(f"Error: {e}")
            speak("I am sorry, I faced an error processing that request.")

          
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            
            if "jarvis" in word.lower():
                speak("Ya, what can i do for you")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    # This displays your actual command on the screen
                    print(f"User (Command): {command}")
                    
                    processCommand(command)
                    
        except Exception as e:
            pass