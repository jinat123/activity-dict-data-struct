spacetelescopesmissions = {
    "Hubble Space Telescope": "Observing distant galaxies and nebulae",
    "James Webb Space Telescope": "Studying the early universe and exoplanets",
    "Chandra X-ray Observatory": "Observing X-ray emissions from black holes",
    "Kepler Space Telescope": "Searching for Earth-like exoplanets",
    "Spitzer Space Telescope": "Studying the infrared universe"
}

entire_dict_telescopes = spacetelescopesmissions

third_telescope = list(spacetelescopesmissions.keys())[2]
third_telescope_mission = spacetelescopesmissions[third_telescope]

first_telescope = list(spacetelescopesmissions.keys())[0]
spacetelescopesmissions[first_telescope] = "Updated mission for deep space observation"

fourth_telescope = list(spacetelescopesmissions.keys())[3]
del spacetelescopesmissions[fourth_telescope]

last_key_value_pair_telescopes = list(spacetelescopesmissions.items())[-1]