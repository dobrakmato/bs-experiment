import os
import numpy as np

from functions import list_songs
from spectrogram import spectrogram

os.makedirs('./spectro', exist_ok=True)

diff = 'expert'
precision = 2

for f in list_songs(diff):
    H = spectrogram(f, precision)
    np.save(f'./spectro/{f}', H)
