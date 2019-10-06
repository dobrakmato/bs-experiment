from functions import list_songs, load_metadata

non_zero = 0
zero = 0

for x in list_songs('expert'):
    meta = load_metadata(x)
    if meta['_songTimeOffset'] != 0:
        non_zero += 1
    else:
        zero += 1

print('zero=', zero)
print('non_zero=', non_zero)
