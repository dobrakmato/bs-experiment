import os

from functions import load_metadata

os.makedirs('./beatmaps', exist_ok=True)
os.makedirs('./beatmaps/easy', exist_ok=True)
os.makedirs('./beatmaps/normal', exist_ok=True)
os.makedirs('./beatmaps/hard', exist_ok=True)
os.makedirs('./beatmaps/expert', exist_ok=True)
os.makedirs('./beatmaps/expertplus', exist_ok=True)
os.makedirs('./beatmaps/metadata', exist_ok=True)
os.makedirs('./beatmaps/ogg', exist_ok=True)

for f in os.listdir('./songs'):
    # metadata
    os.rename(f'./songs/{f}/info.dat', f'./beatmaps/metadata/{f}.json')
    metadata = load_metadata(f)

    # song
    song_name = metadata['_songFilename']
    os.rename(f'./songs/{f}/{song_name}', f'./beatmaps/ogg/{f}.ogg')

    # beatmaps
    for d in ['Easy', 'Normal', 'Hard', 'Expert', 'ExpertPlus']:
        if os.path.exists(f'./songs/{f}/{d}.dat'):
            os.rename(f'./songs/{f}/{d}.dat', f'./beatmaps/{d.lower()}/{f}.json')

print('easy maps=', len(os.listdir('./beatmaps/easy')))
print('normal maps=', len(os.listdir('./beatmaps/normal')))
print('hard maps=', len(os.listdir('./beatmaps/hard')))
print('expert maps=', len(os.listdir('./beatmaps/expert')))
print('expertplus maps=', len(os.listdir('./beatmaps/expertplus')))
print('songs=', len(os.listdir('./beatmaps/metadata')))
