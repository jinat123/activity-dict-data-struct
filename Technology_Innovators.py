technologiesinnovators = {
    "Internet": "Vint Cerf and Bob Kahn",
    "Smartphone": "Steve Jobs",
    "World Wide Web": "Tim Berners-Lee",
    "Personal Computer": "Bill Gates and Paul Allen",
    "Electric Car": "Elon Musk",
    "Light Bulb": "Thomas Edison",
    "Airplane": "Wright Brothers",
    "Blockchain": "Satoshi Nakamoto"
}

entire_dict_technologies = technologiesinnovators

fourth_technology = list(technologiesinnovators.keys())[3]
fourth_technology_innovator = technologiesinnovators[fourth_technology]

second_technology = list(technologiesinnovators.keys())[1]
technologiesinnovators[second_technology] = "Updated Innovator"

sixth_technology = list(technologiesinnovators.keys())[5]
del technologiesinnovators[sixth_technology]

last_key_value_pair_technologies = list(technologiesinnovators.items())[-1]