import math
import struct
import librosa
import numpy as np
import soundfile
import matplotlib.pyplot as plt


def metronome(sample_rate=44100, length=0.05, volume=0.8, freq=1300):
    for step in range(0, int(sample_rate * length)):
        f = step / sample_rate
        yield math.sin(freq * f * math.pi * 2) * volume


H = np.load('bsmap.npy', allow_pickle=True)
clip, sample_rate = librosa.load('song.wav', None)

notes_in_segments = np.sum(H, axis=1)

print("H.shape", H.shape)
print("notes_in_segments.shape", notes_in_segments.shape)

bpm = 174  # todo: load???
one_beat_length = 60 / bpm
one_segment_length_secs = one_beat_length / 2  # to get 1/32

print('bpm=', bpm)
print('one_beat_length=', one_beat_length)
print('one_segment_length_secs=', one_segment_length_secs)

samples_with_notes = []
for i, x in enumerate(np.nditer(notes_in_segments)):
    if x > 0:  # any notes in this segment
        secs = i * one_segment_length_secs
        samples_with_notes.append(int(secs * sample_rate))

result = []
met = None
for i, x in enumerate(np.nditer(clip)):
    if i in samples_with_notes:
        samples_with_notes.remove(i)
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
print('done')
