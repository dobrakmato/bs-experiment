import os
import numpy as np

from beatmap2numpy import beatmap2numpy
from functions import list_songs

os.makedirs('./labels', exist_ok=True)

# settings
diff = 'expert'
precision = 2

empty_segments = 0
collision_count = 0
total_segments = 0
perc_empty = 0
perc_collisions = 0
maps = 0

offenders = []

for f in list_songs(diff):
    H, bpm, es, cc, seg = beatmap2numpy(f, diff, precision)
    empty_segments += es
    collision_count += cc
    total_segments += seg
    perc_empty += 100 * es / seg
    perc_collisions += 100 * cc / seg
    maps += 1

    if cc > 0:
        offenders.append((cc, f))

    np.save(f'./labels/{f}', np.rot90(H))

print('============================================================')
print('precision=', precision)
print('maps=', maps)
print('total segments=', total_segments)
print('empty seg=', empty_segments)
print('collisions=', collision_count)
print('avg empty seg=', empty_segments / maps)
print('avg collisions=', collision_count / maps)
print('avg % empty=', perc_empty / maps)
print('avg % collisions=', perc_collisions / maps)
print('offenders:', len(offenders))
print('=============================================================')

for o in reversed(sorted(offenders, key=lambda x: x[0])):
    print(o[0], o[1])
