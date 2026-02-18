🎙️ Jarvis – Python Voice Assistant
📌 About This Project

I built Jarvis as a Python-based voice assistant to explore how speech recognition, automation, and AI models can work together in a single application.
This project listens for a wake word (“Jarvis”), accepts voice commands, performs predefined actions, and intelligently responds to unknown queries using an AI language model.

The main goal of this project is learning by building — combining core Python concepts with real-world libraries and APIs.

🧠 What Jarvis Can Do

Responds to voice commands after detecting the wake word “Jarvis”

Opens commonly used websites like:

Google

YouTube

LinkedIn

Facebook

LeetCode

Plays music from:

A custom local music library

YouTube (fallback if the song is not found)

Lists available songs from the music library

Fetches and reads out the latest news headlines

Answers general questions using an AI model when no predefined command matches

Speaks all responses using text-to-speech

🧠 Programming Concepts Used

Functions

Conditional statements

Loops

Speech recognition

Text-to-speech

API integration

Error handling

Fuzzy string matching

Environment variables (for security)

🛠️ Technologies & Libraries Used

Python 3

speech_recognition

pyttsx3

webbrowser

requests

difflib

pywhatkit

pygame

gTTS (optional alternative TTS)

Groq API (LLaMA 3.3 – 70B model)

🔐 Important Security Note

This project does NOT store API keys in the source code.

Before running the project, you must set the required API keys as environment variables.

Required Environment Variables

GROQ_API_KEY → For AI responses

NEWS_API_KEY → For fetching news headlines

Example (Windows – PowerShell)
setx GROQ_API_KEY "your_groq_api_key_here"
setx NEWS_API_KEY "your_news_api_key_here"


Restart the terminal after setting them.

📂 Project Structure
Jarvis/
│
├── Jarvis.py          # Main application logic
├── musicLibrary.py   # Dictionary of song names and URLs
├── README.md         # Project documentation
├── .gitignore

▶️ How to Run the Project

Make sure Python 3 is installed.

Install required dependencies:

pip install -r requirements.txt


Navigate to the project directory.

Run the program:

python Jarvis.py


Say “Jarvis” to activate the assistant and give a command.

🗣️ Example Voice Commands

“Jarvis open Google”

“Jarvis play music”

“Jarvis play believer”

“Jarvis list songs”

“Jarvis news”

“Jarvis what is cloud computing”

✨ Key Features

Fully voice-controlled interaction

Clean, function-based design

Intelligent fallback using AI for unknown commands

Simple and extendable code structure

Beginner-friendly but realistic project

⚠️ Current Limitations

No GUI (console-based only)

Limited error feedback for speech recognition failures

Chrome close command is Windows-specific

No multi-language support yet

🚀 Possible Future Improvements

Add GUI (Tkinter / PyQt)

Improve speech recognition accuracy

Add custom wake-word engine

Make it cross-platform

Convert to async execution

Add logging and configuration files

👤 Author

Koteswar Rao Golagani

📜 License

This project is created for learning and educational purposes.
You are free to explore, modify, and build on top of it.
