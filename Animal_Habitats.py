animalshabitats = {
    "Lion": "Savannah",
    "Penguin": "Antarctica",
    "Elephant": "Grasslands",
    "Polar Bear": "Arctic",
    "Kangaroo": "Australian Outback",
    "Panda": "Bamboo Forests",
    "Tiger": "Rainforest",
    "Dolphin": "Oceans"
}

entire_dict_animals = animalshabitats

third_animal = list(animalshabitats.keys())[2]
third_animal_habitat = animalshabitats[third_animal]

fifth_animal = list(animalshabitats.keys())[4]
animalshabitats[fifth_animal] = "Updated Habitat"

seventh_animal = list(animalshabitats.keys())[6]
del animalshabitats[seventh_animal]

last_key_value_pair_animals = list(animalshabitats.items())[-1]