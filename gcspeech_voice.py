import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/user/arcane-atom-257306-cd221017999a.json'
# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # adjust the microphone's energy threshold to ambient noise levels
    r.adjust_for_ambient_noise(source)
    # listen for audio input from the user
    audio = r.listen(source)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code="en-US",
)

client = speech.SpeechClient()

try:
    # recognize speech using Google Cloud Speech-to-Text API
    transcript = client.recognize(config=config, audio=speech.RecognitionAudio(content=audio.get_wav_data())).results[0].alternatives[0].transcript
    print("You said: " + transcript)
except IndexError:
    print("No speech detected")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Cloud Speech-to-Text API service; {0}".format(e))

