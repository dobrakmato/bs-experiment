import os
import time

import requests
import zipfile


def get_top_songs(n=100):
    result = []
    page = 0
    while len(result) < n:
        print(f'[get_top_songs] crawling page {page + 1}')
        time.sleep(2)  # to not get too many requests
        j = requests.get(f'https://beatsaver.com/api/maps/rating/{page}').json()
        for doc in j['docs']:
            result.append('https://beatsaver.com' + doc['directDownload'])

        page += 1
    return result


def download_and_unzip_top_songs(n=50):
    songs = get_top_songs(n)
    for idx, song in enumerate(songs):
        filename = song[song.rfind("/") + 1:]

        if not os.path.isdir('./songs/' + filename[:filename.rfind('.')] + '/'):
            print(f'[download] ({idx + 1}/{len(songs)}) {song}')
            r = requests.get(song)
            open('./download/' + filename, 'wb').write(r.content)

            try:
                with zipfile.ZipFile('./download/' + filename, 'r') as zf:
                    print(f'[unzip] ({idx + 1}/{len(songs)}) {song}')
                    zf.extractall('./songs/' + filename[:filename.rfind('.')] + '/')
            except:
                print(f"[unzip] cannot unzip file {song}!")
        else:
            print(f'[download] ({idx + 1}/{len(songs)}) {song} already exists!')


os.makedirs('./download', exist_ok=True)
os.makedirs('./songs', exist_ok=True)
download_and_unzip_top_songs()
