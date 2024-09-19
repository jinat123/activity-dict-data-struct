dogbreedssizes = {
    "Chihuahua": "Small",
    "Beagle": "Medium",
    "Labrador Retriever": "Large",
    "German Shepherd": "Large",
    "Cocker Spaniel": "Medium",
    "Bulldog": "Medium",
    "Golden Retriever": "Large",
    "Pomeranian": "Small",
    "Great Dane": "Large",
    "Poodle": "Medium"
}

entire_dict_dogs = dogbreedssizes

fifth_breed = list(dogbreedssizes.keys())[4]
fifth_breed_size = dogbreedssizes[fifth_breed]

eighth_breed = list(dogbreedssizes.keys())[7]
dogbreedssizes[eighth_breed] = "Updated Size"

sixth_breed = list(dogbreedssizes.keys())[5]
del dogbreedssizes[sixth_breed]

last_key_value_pair_dogs = list(dogbreedssizes.items())[-1]