import time
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

# Use the same GPIO pin you connected the transistor's base to
buzzer_pin = 18

buzzer = TonalBuzzer(buzzer_pin)

# Define a simple melody using MIDI note numbers
melody = [60, 62, 64, 65, 67, 69, 71, 72]

# Play the melody
for note in melody:
    buzzer.play(Tone(midi=note))
    time.sleep(0.5)
    buzzer.stop()
    time.sleep(0.1)

# Clean up and exit
buzzer.stop()

