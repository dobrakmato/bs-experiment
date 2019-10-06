import math
import struct
import librosa
import numpy as np
import soundfile
import matplotlib.pyplot as plt

clip, sample_rate = librosa.load('beatmaps/ogg/9d31d3aab3d58ab540df63caed06d62ff1cfefdd.ogg', None)
# beats = librosa.onset.onset_detect(clip, sample_rate, units='samples')
tempo, beats = librosa.beat.beat_track(clip, sample_rate, units='samples')

print("clip.shape=", clip.shape)
print("tempo=", tempo)
print("len(beats)=", len(beats))
print("first_beat=", beats[0])

soundfile.write("song.wav", clip[0:], sample_rate)
