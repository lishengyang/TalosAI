import openai
from gtts import gTTS
from io import BytesIO
import pygame
import speech_recognition as sr

openai.api_key = "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"
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
def speak(text):
    with BytesIO() as file:
        tts = gTTS(text=text, lang='zh-CN')
        tts.write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language='zh-CN')
        print("You said: " + text)
        return text
    except Exception as e:
        print("Error: " + str(e))
        return ""

def generate_answer(message):
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat.choices[0].message.content
    return reply



if __name__ == '__main__':
    while True:
        try:
            user_input = listen()
            if not user_input:
                continue
            output = generate_answer(user_input)
            speak(output)
        except KeyboardInterrupt:
            break
