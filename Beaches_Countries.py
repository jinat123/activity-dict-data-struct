beacheslocations = {
    "Bondi Beach": "Australia",
    "Copacabana Beach": "Brazil",
    "Waikiki Beach": "USA",
    "Anse Source d'Argent": "Seychelles",
    "Whitehaven Beach": "Australia",
    "Navagio Beach": "Greece",
    "Seven Mile Beach": "Jamaica",
    "Maya Bay": "Thailand"
}

entire_dict_beaches = beacheslocations

third_beach = list(beacheslocations.keys())[2]
third_beach_country = beacheslocations[third_beach]

sixth_beach = list(beacheslocations.keys())[5]
beacheslocations[sixth_beach] = "Updated Country"

fifth_beach = list(beacheslocations.keys())[4]
del beacheslocations[fifth_beach]

last_key_value_pair_beaches = list(beacheslocations.items())[-1]