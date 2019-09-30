import math
import struct
import librosa
import numpy as np
import soundfile
import matplotlib.pyplot as plt


def metronome(sample_rate=44100, length=0.05, volume=0.5, freq=1200):
    for step in range(0, int(sample_rate * length)):
        f = step / sample_rate
        yield math.sin(freq * f * math.pi * 2) * volume


clip, sample_rate = librosa.load('song.wav', None)
beats = librosa.onset.onset_detect(clip, sample_rate, units='samples')

print("len(beats)=", len(beats))

result = []
met = None
for i, x in enumerate(np.nditer(clip)):
    if i in beats:
        met = iter(metronome())

    if met is not None:
        try:
            v = next(met)
            result.append(x + v)
        except StopIteration:
            result.append(x)
            met = None
    else:
        result.append(x)

soundfile.write("onset.wav", result, sample_rate)
