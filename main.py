import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import pvporcupine
import pyaudio
import struct
import threading

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key="")  # replace with your OpenAI key
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google. Be brief."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    c = c.lower()

    if c in ["goodbye"]:
        speak("Goodbye Amogh. See you later!")
        exit()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play "):
        song = c.split("play ", 1)[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    else:
        response = aiProcess(c)
        speak(response)

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            processCommand(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            speak("Speech recognition service error.")

def jarvis_loop():
    porcupine = pvporcupine.create(access_key="", keywords=["jarvis"])  # You can change to 'hey jarvis' with custom model
    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    speak("Hi, I am Jarvis. Say 'Jarvis' to wake me.")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("Wake word detected!")
                speak("Yes Amogh, how can I help?")
                listen_for_command()

    except KeyboardInterrupt:
        print("Stopping Jarvis...")
    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    jarvis_loop()
