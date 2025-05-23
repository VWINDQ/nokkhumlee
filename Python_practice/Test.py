Liked_songs = {
    'We cant be friends': 'Ariana Grande',
    'Supernatural': 'Ariana Grande',
    'Love me harder': 'Ariana Grande',
    'Die for you': 'The Weeknd',
    'Save your tears': 'The Weeknd',
    'Call out my name': 'The Weeknd',
    'Blinding lights': 'The Weeknd',
}

def write_liked_songs(songs, filename):
    with open(filename, 'w') as file:
        file.write('Liked_song:\n')
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")

write_liked_songs(Liked_songs, "liked_songs.txt")