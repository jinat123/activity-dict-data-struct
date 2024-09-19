planetsdistances = {
    "Mercury": 57.9,
    "Venus": 108.2,
    "Earth": 149.6,
    "Mars": 227.9,
    "Jupiter": 778.5,
    "Saturn": 1434,
    "Uranus": 2871,
    "Neptune": 4495
}

entire_dict_planets = planetsdistances

third_planet = list(planetsdistances.keys())[2]
third_planet_distance = planetsdistances[third_planet]

fifth_planet = list(planetsdistances.keys())[4]
planetsdistances[fifth_planet] = 780  # Updated distance

seventh_planet = list(planetsdistances.keys())[6]
del planetsdistances[seventh_planet]

last_key_value_pair_planets = list(planetsdistances.items())[-1]