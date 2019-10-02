import os

from download_top_songs import download_and_unzip_top_songs
from separate_diffuculties import organized_unzipped_songs
from convert_to_dataset import generate_script_for_difficulty

song_count = 1500

os.makedirs('./training', exist_ok=True)
os.makedirs('./songs', exist_ok=True)
os.makedirs('./download', exist_ok=True)
os.makedirs('./difficulties', exist_ok=True)
os.makedirs('./difficulties/easy', exist_ok=True)
os.makedirs('./difficulties/normal', exist_ok=True)
os.makedirs('./difficulties/hard', exist_ok=True)
os.makedirs('./difficulties/expert', exist_ok=True)
os.makedirs('./difficulties/expertplus', exist_ok=True)

# download_and_unzip_top_songs(song_count)
# organized_unzipped_songs()

for difficulty in ['easy', 'normal', 'hard', 'expert', 'expertplus']:
    with open(f'./training/{difficulty}.txt', 'wb') as f:
        f.write(generate_script_for_difficulty(difficulty).encode('utf-8'))
