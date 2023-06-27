import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # adjust the microphone's energy threshold to ambient noise levels
    r.adjust_for_ambient_noise(source)
    # listen for audio input from the user
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

