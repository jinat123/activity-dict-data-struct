albumsyears = {
    "Thriller": 1982,
    "Back in Black": 1980,
    "The Dark Side of the Moon": 1973,
    "The Wall": 1979,
    "Abbey Road": 1969,
    "Hotel California": 1976,
    "Born in the USA": 1984,
    "Rumours": 1977,
    "Nevermind": 1991,
    "Purple Rain": 1984
}

entire_dict_albums = albumsyears

third_album = list(albumsyears.keys())[2]
third_album_year = albumsyears[third_album]

eighth_album = list(albumsyears.keys())[7]
albumsyears[eighth_album] = 1978  # Updated release year

fifth_album = list(albumsyears.keys())[4]
del albumsyears[fifth_album]

last_key_value_pair_albums = list(albumsyears.items())[-1]