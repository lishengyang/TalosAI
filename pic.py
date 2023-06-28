import os
from gtts import gTTS
import pygame

# Set up Pygame audio
pygame.mixer.init()

# Capture an image
os.system("fswebcam -r 1280x720 image.jpg")

# Generate and play a spoken message
print("Picture taken!")
tts = gTTS("Picture taken!")
tts.save("picture_taken.mp3")
pygame.mixer.music.load("picture_taken.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

