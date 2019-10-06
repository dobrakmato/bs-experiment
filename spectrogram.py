import librosa
from functions import load_metadata, path_to_song


def spectrogram(song, precision=2, fmax=10000, fmin=0, n_mels=128):
    meta = load_metadata(song)
    bpm = meta['_beatsPerMinute']
    clip, sample_rate = librosa.load(path_to_song(song), None)

    clip_length = len(clip) / sample_rate

    # 1 beat = quarter note
    samples_per_beat = 60 * sample_rate / bpm
    samples_per_segment = samples_per_beat / precision  # to get 1/32

    print("bpm=", bpm)
    print("precision=", precision)
    print("clip_length=", clip_length)
    print("samples_per_beat=", samples_per_beat)
    print("samples_per_segment=", samples_per_segment)

    mel_spec = librosa.feature.melspectrogram(clip, n_fft=10240, hop_length=int(samples_per_segment), sr=sample_rate,
                                              fmin=fmin, fmax=fmax, n_mels=n_mels)

    print(mel_spec.shape)

    # librosa.display.specshow(librosa.amplitude_to_db(mel_spec, ref=np.max),
    #       y_axis='log', x_axis='time', sr=sample_rate)
    # plt.title('melspectrogram')
    # plt.colorbar(format='%+2.0f dB')
    # plt.tight_layout()
    # plt.show()

    return mel_spec
