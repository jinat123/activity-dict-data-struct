moviegenres = {
    "Action": "Mad Max: Fury Road",
    "Comedy": "The Hangover",
    "Drama": "The Shawshank Redemption",
    "Horror": "The Conjuring",
    "Science Fiction": "Interstellar",
    "Romance": "The Notebook",
    "Fantasy": "The Lord of the Rings",
    "Thriller": "Se7en"
}

entire_dict_genres = moviegenres

third_genre = list(moviegenres.keys())[2]
third_genre_movie = moviegenres[third_genre]

fifth_genre = list(moviegenres.keys())[4]
moviegenres[fifth_genre] = "Updated Movie"

seventh_genre = list(moviegenres.keys())[6]
del moviegenres[seventh_genre]

last_key_value_pair_genres = list(moviegenres.items())[-1]