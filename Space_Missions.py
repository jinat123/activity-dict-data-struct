spacemissions = {
    "Apollo 11": 1969,
    "Voyager 1": 1977,
    "Mars Rover Curiosity": 2012,
    "SpaceX Falcon Heavy": 2018,
    "Perseverance Rover": 2020
}

entire_dict_missions = spacemissions

third_mission = list(spacemissions.keys())[2]
third_mission_year = spacemissions[third_mission]

second_mission = list(spacemissions.keys())[1]
spacemissions[second_mission] = 1978  # Updated year

fourth_mission = list(spacemissions.keys())[3]
del spacemissions[fourth_mission]

last_key_value_pair_missions = list(spacemissions.items())[-1]