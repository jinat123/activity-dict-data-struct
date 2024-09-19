moviedirector = {
    "Inception": "Christopher Nolan",
    "Pulp Fiction": "Quentin Tarantino",
    "The Godfather": "Francis Ford Coppola",
    "The Dark Knight": "Christopher Nolan",
    "Fight Club": "David Fincher",
    "The Lord of the Rings": "Peter Jackson",
    "Avatar": "James Cameron",
    "Titanic": "James Cameron",
    "The Matrix": "The Wachowskis",
    "Interstellar": "Christopher Nolan"
}

entire_dict_movies = moviedirector

fifth_movie = list(moviedirector.keys())[4]
fifth_movie_director = moviedirector[fifth_movie]

ninth_movie = list(moviedirector.keys())[8]
moviedirector[ninth_movie] = "Updated Director"

seventh_movie = list(moviedirector.keys())[6]
del moviedirector[seventh_movie]

last_key_value_pair_movies = list(moviedirector.items())[-1]