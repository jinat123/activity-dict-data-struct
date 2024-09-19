citieslandmarks = {
    "Paris": "Eiffel Tower",
    "New York": "Statue of Liberty",
    "London": "Big Ben",
    "Rome": "Colosseum",
    "Sydney": "Sydney Opera House",
    "Tokyo": "Tokyo Tower",
    "Cairo": "Pyramids of Giza",
    "Beijing": "Great Wall of China"
}

entire_dict_cities = citieslandmarks

sixth_city = list(citieslandmarks.keys())[5]
sixth_city_landmark = citieslandmarks[sixth_city]

second_city = list(citieslandmarks.keys())[1]
citieslandmarks[second_city] = "Empire State Building"  # Updated landmark

seventh_city = list(citieslandmarks.keys())[6]
del citieslandmarks[seventh_city]

last_key_value_pair_cities = list(citieslandmarks.items())[-1]