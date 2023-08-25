def movie_organizer(*name_genre):
    movie_collection = {}
    for i in range(len(name_genre)):
        if name_genre[i][1] not in movie_collection:
            movie_collection[name_genre[i][1]] = []
        movie_collection[name_genre[i][1]].append(name_genre[i][0])

    sorted_collection = sorted(movie_collection.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for genre, movie_name in sorted_collection:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()


print(movie_organizer(
    ("The Matrix", "Sci-fi")))