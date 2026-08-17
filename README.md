# Voice-Based AI Assistant

A simple AI assistant that takes a user's voice input, converts it into text, generates a simple explanation using an LLM, and converts the response back into speech.

## Features

* Voice input using a microphone
* Speech-to-text using Google Speech Recognition
* AI-generated explanations using an LLM
* LangChain PromptTemplate integration
* Text-to-speech using gTTS
* Saves the generated response as an MP3 file

## Technologies Used

* Python
* SpeechRecognition
* LangChain
* OpenRouter
* OpenAI-compatible LLM
* gTTS
* python-dotenv

## How It Works

```text
Voice Input
    ↓
Speech-to-Text
    ↓
LLM
    ↓
Simple Explanation
    ↓
Text-to-Speech
    ↓
AIVoice.mp3
```

## Installation

Install the required packages:

```bash
pip install SpeechRecognition langchain-openai langchain python-dotenv gTTS PyAudio
```

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key
```

Run the application:

```bash
python AI_assistant.py
```

Speak a topic when prompted. The AI will generate a simple explanation and save it as `AIVoice.mp3`.

## Note

Do not upload your `.env` file or API key to GitHub.

## Author

Sushmitha J N
