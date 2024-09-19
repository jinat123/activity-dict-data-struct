plantstypes = {
    "Rose": "Shrub",
    "Oak": "Tree",
    "Basil": "Herb",
    "Cactus": "Succulent",
    "Lavender": "Herb",
    "Maple": "Tree",
    "Fern": "Fern",
    "Sunflower": "Herb"
}

entire_dict_plants = plantstypes
    
fifth_plant = list(plantstypes.keys())[4]
fifth_plant_type = plantstypes[fifth_plant]

second_plant = list(plantstypes.keys())[1]
plantstypes[second_plant] = "Updated Type"

sixth_plant = list(plantstypes.keys())[5]
del plantstypes[sixth_plant]

last_key_value_pair_plants = list(plantstypes.items())[-1]