import google.cloud.texttospeech as tts
import google.cloud.speech_v1p1beta1 as speech
import os
import wave
import pyaudio
import tempfile

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/orangepi/arcane-atom-257306-cd221017999a.json'

# Define command mapping
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

# Convert command mapping to WAV files
def text_to_wav(voice_name: str, text: str, output_file: str):
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

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    print(f'Generated speech saved to "{output_file}"')

for command, options in command_mapping.items():
    wav_file = command + '.wav'
    text_to_wav("en-US-Wavenet-D", f"{command}", wav_file)
    for option in options:
        text_to_wav("en-US-Wavenet-D", f"{option} is a {command}", option + '.wav')

# Listen to microphone input and recognize commands
def listen_for_commands():
    # create a recognizer object
    r = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    client = speech.SpeechClient()

    with tempfile.NamedTemporaryFile(mode='wb', suffix='.wav', delete=False) as f:
        # use the default microphone as the audio source
        with pyaudio.PyAudio() as audio:
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            print("Say something!")
            while True:
                data = stream.read(1024)
                f.write(data)
                try:
                    # recognize speech using Google Cloud Speech-to-Text API
                    transcript = client.recognize(config=r, audio=speech.RecognitionAudio(content=data)).results[0].alternatives[0].transcript
                    print("You said: " + transcript)

                    # check if recognized command is in the command mapping
                    for command, options in command_mapping.items():
                        if command in transcript:
                            for option in options:
                                if option in transcript:
                                    option_wav_file = option + '.wav'
                                    play_wav(option_wav_file)
                                    break

                except IndexError:
                    pass
                except speech.errors.OutOfRange as e:
                    print(e)
                    break
                except Exception as e:
                    print(e)
                    break

def play_wav(filename):
    # Load the WAV file and play it through the speakers

def play_wav(filename):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Read data and play stream
    data = wf.readframes(1024)

    while data:
        stream.write(data)
        data = wf.readframes(1024)

    # Stop stream
    stream.stop_stream()
    stream.close()

    # Close PyAudio
    p.terminate()

