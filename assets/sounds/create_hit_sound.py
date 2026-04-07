import numpy as np
import soundfile as sf
import math

# Sound settings
sample_rate = 44100
duration = 0.25     # seconds
frequency = 800     # hit sound pitch
volume = 32767

filename = "hit.ogg"

num_samples = int(sample_rate * duration)
samples = np.array([
    int(volume * math.sin(2 * math.pi * frequency * i / sample_rate))
    for i in range(num_samples)
], dtype=np.int16)

sf.write(filename, samples, sample_rate, format='OGG', subtype='VORBIS')

print("✅ hit.ogg created successfully")