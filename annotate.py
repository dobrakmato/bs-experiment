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


H = np.load('bsmap.npy')
clip, sample_rate = librosa.load('song.wav', None)

notes_in_segments = np.sum(H, axis=1)

print("H.shape", H.shape)
print("notes_in_segments.shape", notes_in_segments.shape)

bpm = 166  # todo: load???
one_beat_length = 60 / bpm
one_segment_length_secs = one_beat_length / 8  # to get 1/32
one_segment_length_samples = int(one_segment_length_secs * sample_rate)

print('bpm=', bpm)
print('one_beat_length=', one_beat_length)
print('one_segment_length_secs=', one_segment_length_secs)

samples_with_notes = []
for i, x in enumerate(np.nditer(notes_in_segments)):
    if x > 0:
        secs = i * one_segment_length_secs
        samples_with_notes.append(secs * sample_rate/4)

print('result')
result = []
met = None
for i, x in enumerate(np.nditer(clip)):
    if i in samples_with_notes:
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

soundfile.write("annotated.wav", result, sample_rate)
