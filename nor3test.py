import os
import speech_recognition as sr
import google.cloud.texttospeech as tts
import subprocess
from google.cloud import speech_v1p1beta1 as speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/orangepi/arcane-atom-257306-cd221017999a.json'

command_mapping = {
    "restaurant": [
        "McDonald's",
        "Subway",
        "KFC",
        "Pizza Hut",
        "Starbucks"
    ],
    "food shop": [
        "Burger King",
        "Taco Bell",
        "Wendy's",
        "Chipotle",
        "Dunkin'"
    ],
    "snack": [
        "Cinnabon",
        "Jamba",
        "Auntie Anne's",
        "Krispy Kreme",
        "Pretzel Maker"
    ],
}

def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
    return filename

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # adjust the microphone's energy threshold to ambient noise levels
    r.adjust_for_ambient_noise(source)
    # listen for audio input from the user
    audio = r.listen(source)

config = sr.Recognizer()
# recognize speech using Google Cloud Speech-to-Text API
try:
    transcript = r.recognize_google_cloud(audio, credentials_json=json_credentials)
    print("You said: " + transcript)
    
    # check if recognized command is in the command mapping
    for command, options in command_mapping.items():
        if command in transcript:
            for option in options:
                if option in transcript:
                    print(f"{option} is a {command}")
                    file = text_to_wav("en-US-Wavenet-D", f"{option} is a {command}")
                    # use aplay to play the audio
                    subprocess.run(["aplay", file])
                    break

except sr.UnknownValueError:
    print("Google Cloud Speech-to-Text API could not understand audio")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Cloud Speech-to-Text API service; {0}".format(e))

