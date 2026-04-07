import numpy as np
import soundfile as sf
import math
import os

# Sound settings
sample_rate = 44100
duration = 0.25     # seconds
frequency = 800     # hit sound pitch
volume = 32767

out_path = os.path.join(os.path.dirname(__file__), 'hit.ogg')

# Generate samples
num_samples = int(sample_rate * duration)
samples = np.array([
    int(volume * math.sin(2 * math.pi * frequency * i / sample_rate))
    for i in range(num_samples)
], dtype=np.int16)

sf.write(out_path, samples, sample_rate, format='OGG', subtype='VORBIS')

print('created hit.ogg')