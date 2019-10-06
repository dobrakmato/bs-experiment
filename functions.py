import json
import os


def list_songs(difficulty):
    return [x.replace('.json', '') for x in os.listdir(f'./beatmaps/{difficulty.lower()}')]


def path_to_song(song):
    return f'./beatmaps/ogg/{song}.ogg'


def load_metadata(song):
    with open(f'./beatmaps/metadata/{song}.json') as f:
        return json.load(f)


def load_beatmap(song, difficulty):
    with open(f'./beatmaps/{difficulty}/{song}.json') as f:
        return json.load(f)
