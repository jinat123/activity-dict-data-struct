technologiesinventors = {
    "Telephone": "Alexander Graham Bell",
    "Light Bulb": "Thomas Edison",
    "World Wide Web": "Tim Berners-Lee",
    "Airplane": "Wright Brothers",
    "Computer": "Charles Babbage",
    "Mobile Phone": "Martin Cooper"
}

entire_dict_technologies = technologiesinventors

fourth_technology = list(technologiesinventors.keys())[3]
fourth_technology_inventor = technologiesinventors[fourth_technology]

second_technology = list(technologiesinventors.keys())[1]
technologiesinventors[second_technology] = "Updated Inventor"

sixth_technology = list(technologiesinventors.keys())[5]
del technologiesinventors[sixth_technology]

last_key_value_pair_technologies = list(technologiesinventors.items())[-1]