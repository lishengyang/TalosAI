from google.cloud import speech_v1p1beta1 as speech
import os
import io

# Setting Google credential
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/orangepi/arcane-atom-257306-cd221017999a.json'

# Create client instance
client = speech.SpeechClient()

# Create recognizer object
recognizer_config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    audio_channel_count=2,
    enable_automatic_punctuation=True
)

# Use the default microphone as the audio source
with speech.Microphone() as source:
    print("Say something!")
    audio = recognizer_config.to_stream(source)

# Sends the request to Google Cloud Speech-to-Text API to transcribe the audio
response = client.recognize(config=recognizer_config, audio=audio)

# Reads the response
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))

