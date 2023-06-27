from google.cloud import speech_v1p1beta1 as speech
import os
import speech_recognition as sr

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

# create a recognizer object
r = sr.Recognizer()

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        # adjust the microphone's energy threshold to ambient noise levels
        r.adjust_for_ambient_noise(source)
        # listen for audio input from the user
        audio = r.listen(source)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    client = speech.SpeechClient()

    try:
        # recognize speech using Google Cloud Speech-to-Text API
        transcript = client.recognize(config=config, audio=speech.RecognitionAudio(content=audio.get_wav_data())).results[0].alternatives[0].transcript
        print("You said: " + transcript)

        # find the command in the transcript and print the corresponding list
        for command, responses in command_mapping.items():
            if command in transcript:
                print(responses)
                break
    except IndexError:
        print("No speech detected")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Cloud Speech-to-Text API service; {0}".format(e))

