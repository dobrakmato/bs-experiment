import json
import numpy as np
import matplotlib.pyplot as plt

from functions import load_metadata, load_beatmap


def beatmap2f24(song, difficulty='expert', precision=2):
    metadata = load_metadata(song)
    beatmap = load_beatmap(song, difficulty)
    notes = list(reversed(sorted(beatmap['_notes'], key=lambda x: x['_time'])))

    bpm = metadata['_beatsPerMinute']
    one_beat_length = 60 / bpm  # len of one beat in seconds
    one_segment_length = one_beat_length / precision  # to get 1/32

    print('track=', metadata['_songAuthorName'], metadata['_songName'])
    print('bpm=', bpm)
    print('last_note(beats)=', notes[0]['_time'])
    print('time(sec)=', notes[0]['_time'] / bpm * 60)
    print('one_beat_length(sec)=', one_beat_length)
    print('one_segment_length(sec)=', one_segment_length)
    print('segments_in_song=', (notes[0]['_time'] / bpm * 60) / one_segment_length)
    print('notes=', len(notes))

    segments = []
    empty_segments = 0
    collision_count = 0
    end_in_secs = one_segment_length

    def to_secs(beats):
        return beats / bpm * 60

    # we loop until we remove all notes from the collection
    while len(notes) != 0:
        segment = [0.0 for _ in range(24)]
        empt = True

        # we take all the notes from the end of notes list (because we reversed the list
        # to allow us to pop() from end) that occur inside this segment (start, end]
        while len(notes) != 0 and to_secs(notes[-1]['_time']) < end_in_secs:
            note = notes.pop()
            idx = note['_lineIndex'] + note['_lineLayer'] * 3

            if note['_type'] == 1:
                idx += 12

            if segment[idx] > 0.0:
                collision_count += 1
            segment[idx] = 1.0
            empt = False

        segments.append(segment)
        if empt:
            empty_segments += 1

        # we go to next segment
        end_in_secs += one_segment_length

    print('segments=', len(segments))
    print('empty segments=', empty_segments, 100 * empty_segments / len(segments))
    print('collisions=', collision_count, 100 * collision_count / len(segments))
    H = np.array(segments)
    print('H.shape', H.shape)

    # plt.imshow(H, aspect='auto', interpolation='sinc', vmin=0, vmax=0.03)
    # plt.show()

    # np.save('bsmap', H)
    return H, bpm, empty_segments, collision_count, len(segments)


def beatmap2onset(song, difficulty='expert', precision=2):
    metadata = load_metadata(song)
    beatmap = load_beatmap(song, difficulty)
    notes = list(reversed(sorted(beatmap['_notes'], key=lambda x: x['_time'])))

    bpm = metadata['_beatsPerMinute']
    one_beat_length = 60 / bpm  # len of one beat in seconds
    one_segment_length = one_beat_length / precision  # to get 1/32

    print('track=', metadata['_songAuthorName'], metadata['_songName'])
    print('bpm=', bpm)
    print('last_note(beats)=', notes[0]['_time'])
    print('time(sec)=', notes[0]['_time'] / bpm * 60)
    print('one_beat_length(sec)=', one_beat_length)
    print('one_segment_length(sec)=', one_segment_length)
    print('segments_in_song=', (notes[0]['_time'] / bpm * 60) / one_segment_length)
    print('notes=', len(notes))

    segments = []
    end_in_secs = one_segment_length

    def to_secs(beats):
        return beats / bpm * 60

    # we loop until we remove all notes from the collection
    while len(notes) != 0:
        has = False

        # we take all the notes from the end of notes list (because we reversed the list
        # to allow us to pop() from end) that occur inside this segment (start, end]
        while len(notes) != 0 and to_secs(notes[-1]['_time']) < end_in_secs:
            note = notes.pop()
            has = True

        segments.append(1.0 if has else 0.0)

        # we go to next segment
        end_in_secs += one_segment_length

    print('segments=', len(segments))

    H = np.array(segments)
    print('H.shape', H.shape)

    return H, bpm, 0, 0, len(segments)
