festivalslocations = {
    "Carnival": "Brazil",
    "Oktoberfest": "Germany",
    "Diwali": "India",
    "Mardi Gras": "New Orleans, USA",
    "Chinese New Year": "China",
    "Running of the Bulls": "Spain",
    "Day of the Dead": "Mexico",
    "La Tomatina": "Spain"
}

entire_dict_festivals = festivalslocations

fourth_festival = list(festivalslocations.keys())[3]
fourth_festival_location = festivalslocations[fourth_festival]

sixth_festival = list(festivalslocations.keys())[5]
festivalslocations[sixth_festival] = "Updated Location"

second_festival = list(festivalslocations.keys())[1]
del festivalslocations[second_festival]

last_key_value_pair_festivals = list(festivalslocations.items())[-1]