import os
from datetime import datetime
from gtts import gTTS
import pygame
import time

# Set up Pygame audio
pygame.mixer.init()

# Capture a video
resolution = "1280x720"
fps = "30"
duration = "10"
now = datetime.now()
filename = f"video_{now.strftime('%Y%m%d_%H%M%S')}.mp4"
command = f"ffmpeg -f v4l2 -video_size {resolution} -framerate {fps} -i /dev/video0 -t {duration} -f alsa -i default -acodec aac -strict experimental -ab 128k -ar 44100 -async 1 -y {filename}"
os.system(command + " & sleep " + duration + " && pkill -INT ffmpeg")

# Generate and play a spoken message
print("Video captured!")
tts = gTTS("Video captured!")
tts.save("video_captured.mp3")
pygame.mixer.music.load("video_captured.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

# Print the creation time of the video
creation_time = os.path.getmtime(filename)
print(f"Video created on {time.ctime(creation_time)}")

