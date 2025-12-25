import wave
import struct
import math
import os

# Sound settings
sample_rate = 44100
duration = 0.25     # seconds
frequency = 800     # hit sound pitch
volume = 32767

out_path = os.path.join(os.path.dirname(__file__), 'hit.wav')

with wave.open(out_path, 'w') as wav:
    wav.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))
    for i in range(int(sample_rate * duration)):
        value = int(volume * math.sin(2 * math.pi * frequency * i / sample_rate))
        wav.writeframes(struct.pack('<h', value))

print('created hit.wav')
