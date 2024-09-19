flowersmeanings = {
    "Rose": "Love",
    "Lily": "Purity",
    "Daisy": "Innocence",
    "Tulip": "Perfect Love",
    "Sunflower": "Adoration",
    "Orchid": "Beauty",
    "Lavender": "Calmness",
    "Lotus": "Enlightenment"
}

entire_dict_flowers = flowersmeanings

fifth_flower = list(flowersmeanings.keys())[4]
fifth_flower_meaning = flowersmeanings[fifth_flower]

seventh_flower = list(flowersmeanings.keys())[6]
flowersmeanings[seventh_flower] = "Updated Meaning"

sixth_flower = list(flowersmeanings.keys())[5]
del flowersmeanings[sixth_flower]

last_key_value_pair_flowers = list(flowersmeanings.items())[-1]