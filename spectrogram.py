import math
import struct
import librosa
import librosa.display
import numpy as np
import soundfile
import matplotlib.pyplot as plt

clip, sample_rate = librosa.load('song.wav', None)
tempo = librosa.beat.tempo(clip, sample_rate)

clip_length = len(clip) / sample_rate

# 1 beat = quarter note
samples_per_beat = 60 * sample_rate / tempo
samples_per_segment = samples_per_beat / 32  # to get 1/32

print("tempo=", tempo)
print("clip_length=", clip_length)
print("samples_per_beat=", samples_per_beat)
print("samples_per_1/32=", samples_per_segment)

# stft = librosa.core.stft(clip, n_fft=1024, hop_length=int(samples_per_segment), sample_rate=sample_rate)
mel_spec = librosa.feature.melspectrogram(clip, n_fft=10240, hop_length=int(samples_per_segment), sr=sample_rate, fmin=0,
                                          fmax=10000, n_mels=128)

print(mel_spec.shape)

librosa.display.specshow(librosa.amplitude_to_db(mel_spec, ref=np.max), y_axis='log', x_axis='time')
plt.title('melspectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()

np.save('spectrogram', mel_spec)
