import json
import numpy as np
import matplotlib.pyplot as plt

name = 'beatsaber'
metadata = json.load(open(f'info/{name}.json'))
beatmap = json.load(open(f'maps/{name}.json'))
notes = list(reversed(beatmap['_notes']))

bpm = metadata['_beatsPerMinute']
one_beat_length = 60 / bpm
one_segment_length = one_beat_length / 8  # to get 1/32
offset = 0

print('bpm=', bpm)
print('one_beat_length=', one_beat_length)
print('one_segment_length=', one_segment_length)
print('offset=', one_beat_length)
print('len(notes)=', len(notes))

segments = []
end = one_segment_length

# we loop until we remove all notes from the collection
while len(notes) != 0:
    segment = [0.0 for _ in range(12)]

    # we take all the notes from the end of notes list (because we reversed the list
    # to allow us to pop() from end) that occur inside this segment (start, end]
    while len(notes) != 0 and notes[-1]['_time'] < end:
        note = notes.pop()
        idx = note['_lineIndex'] + note['_lineLayer'] * 3
        segment[idx] = 1.0

    segments.append(segment)

    # we go to next segment
    end = end + one_segment_length

print('len(segments)=', len(segments))
H = np.array(segments)
print('H.shape', H.shape)

plt.imshow(H)
plt.show()

np.save('bsmap', H)

