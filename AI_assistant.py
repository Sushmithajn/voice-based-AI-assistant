import speech_recognition as sr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from gtts import gTTS
import os

load_dotenv()

prompt = PromptTemplate(
    template = '''
    Assume you are a experienced Trainer Technical with very good knowledge
    you need to generate definition of a give topic in simple terms like one line definition
    Given : {topic}''',
    input_variables = ['topic']
)

llm = ChatOpenAI(
    model = "gpt-4o",
    temperature = 1,
    max_tokens = 200,
    api_key = os.getenv("OPENROUTER_API_KEY"),
    base_url = "https://openrouter.ai/api/v1"
)

recognizer = sr.Recognizer()

with sr.Microphone() as Source:
    print("Speak a topic: ")
    audio = recognizer.listen(Source)

    try :
        text = recognizer.recognize_google(audio)
        print(f"your topic is : {text}")

    except sr.UnknownValueError:
        print("Sorry could not able to understand you voice")


response = llm.invoke(prompt.format(topic = text))
print(response.content)
ans = response.content
final = gTTS(text =ans, lang = 'en')
final.save("AIVoice.mp3")
print("end")
