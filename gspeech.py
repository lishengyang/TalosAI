import io
from google.cloud import speech_v1p1beta1 as speech
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/orangepi/arcane-atom-257306-cd221017999a.json'
client = speech.SpeechClient()

file_name = '/home/orangepi/welcome.wav'

with io.open(file_name, 'rb') as f:
    content = f.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=24000,
    language_code='en-US')

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

