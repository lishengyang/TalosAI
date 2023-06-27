import io
import os
import pyaudio
from google.cloud import speech_v1p1beta1 as speech

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/orangepi/arcane-atom-257306-cd221017999a.json'

# Set up audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
audio = pyaudio.PyAudio()

# Set up Google Cloud Speech client
client = speech.SpeechClient()

# Define streaming audio request generator
def stream_generator():
    with audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK) as stream:
        while True:
            data = stream.read(CHUNK)
            yield speech.RecognitionAudio(content=data)

# Define streaming speech recognition request
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code='en-US',
    model='default',
    enable_automatic_punctuation=True
)
stream_request = speech.StreamingRecognizeRequest(audio_config=config, interim_results=True)

# Start streaming speech recognition
streaming = client.streaming_recognize(stream_request, stream_generator())

# Process streaming speech recognition responses
for response in streaming:
    if response.results:
        for result in response.results:
            if result.is_final:
                print(result.alternatives[0].transcript)
import io
import os
import pyaudio
from google.cloud import speech_v1p1beta1 as speech

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/json/key/file.json'

# Set up audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
audio = pyaudio.PyAudio()

# Set up Google Cloud Speech client
client = speech.SpeechClient()

# Define streaming audio request generator
def stream_generator():
    with audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK) as stream:
        while True:
            data = stream.read(CHUNK)
            yield speech.RecognitionAudio(content=data)

# Define streaming speech recognition request
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code='en-US',
    model='default',
    enable_automatic_punctuation=True
)
stream_request = speech.StreamingRecognizeRequest(audio_config=config, interim_results=True)

# Start streaming speech recognition
streaming = client.streaming_recognize(stream_request, stream_generator())

# Process streaming speech recognition responses
for response in streaming:
    if response.results:
        for result in response.results:
            if result.is_final:
                print(result.alternatives[0].transcript)

