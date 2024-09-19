riverslengths = {
    "Nile": 6650,
    "Amazon": 6400,
    "Yangtze": 6300,
    "Mississippi": 6275,
    "Yenisei": 5539,
    "Yellow River": 5464
}

entire_dict_rivers = riverslengths

second_river = list(riverslengths.keys())[1]
second_river_length = riverslengths[second_river]

fifth_river = list(riverslengths.keys())[4]
riverslengths[fifth_river] = 5600  # Updated length

fourth_river = list(riverslengths.keys())[3]
del riverslengths[fourth_river]

last_key_value_pair_rivers = list(riverslengths.items())[-1]