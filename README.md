# 🧠 Jarvis - Voice Assistant using OpenAI, Wake Word, and Speech Recognition

Jarvis is a voice-controlled personal assistant built in Python. It uses wake-word detection, speech recognition, and OpenAI's GPT model to perform tasks such as answering questions, playing music, opening websites, and more — all via voice commands.

---

## ✨ Features

- 🗣️ Wake word detection using **Porcupine** ("Jarvis")
- 🔊 Voice recognition using **SpeechRecognition**
- 🧠 Conversational responses using **OpenAI GPT-3.5**
- 📢 Text-to-speech using **gTTS + Pygame**
- 🌐 Web browsing automation (Google, YouTube, etc.)
- 🎵 Music playing from a local or custom `musicLibrary`
- 🔐 API key security with `.env` support

---

## 🚀 Tech Stack

- Python 3.10+
- OpenAI API (`openai`)
- Google Text-to-Speech (`gTTS`)
- Pygame (for audio playback)
- SpeechRecognition (Google STT API)
- Porcupine (wake word detection)
- PyAudio (microphone input)
- dotenv (`python-dotenv` for secret management)

---