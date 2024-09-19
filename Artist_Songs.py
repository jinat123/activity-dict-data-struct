artistssongs = {
    "Taylor Swift": "Love Story",
    "Ed Sheeran": "Shape of You",
    "Beyoncé": "Halo",
    "Drake": "God's Plan",
    "Adele": "Someone Like You",
    "The Weeknd": "Blinding Lights",
    "Bruno Mars": "Uptown Funk",
    "Rihanna": "Umbrella"
}

entire_dict_artists = artistssongs

third_artist = list(artistssongs.keys())[2]
third_artist_song = artistssongs[third_artist]

sixth_artist = list(artistssongs.keys())[5]
artistssongs[sixth_artist] = "Updated Top Song"

seventh_artist = list(artistssongs.keys())[6]
del artistssongs[seventh_artist]

last_key_value_pair_artists = list(artistssongs.items())[-1]