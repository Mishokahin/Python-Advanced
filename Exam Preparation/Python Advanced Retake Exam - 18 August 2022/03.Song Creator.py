def add_songs(*args):
    songs = {}
    final = []

    for name, lyrics in args:
        if name not in songs:
            songs[name] = []
        songs[name].extend(lyrics)

    for song in songs:
        final.append(f"- {song}")
        if songs[song]:
            final.extend(songs[song])

    return "\n".join(final)