import functools

playlist = {
    'title': 'patagonia bus',
    'author': 'colt seele',
    'songs': [
        {
            'title': 'song 1',
            'artist': ['blue'],
            'duration': 2.5
        },
        {
            'title': 'song 2',
            'artist': ['Shakira'],
            'duration': 3.15
        }
    ]
}

total_duration = 0

for song in playlist['songs']:
    total_duration += song['duration']

print(total_duration)

#print(type(playlist['songs'][0]['duration']))
#print(functools.reduce(lambda a,b : a+b,str(playlist['songs'].values())))