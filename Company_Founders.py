companiesfounders = {
    "Microsoft": "Bill Gates and Paul Allen",
    "Apple": "Steve Jobs and Steve Wozniak",
    "Amazon": "Jeff Bezos",
    "Google": "Larry Page and Sergey Brin",
    "Facebook": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "SpaceX": "Elon Musk",
    "Alibaba": "Jack Ma"
}

entire_dict_companies = companiesfounders

sixth_company = list(companiesfounders.keys())[5]
sixth_company_founder = companiesfounders[sixth_company]

second_company = list(companiesfounders.keys())[1]
companiesfounders[second_company] = "Updated Founder"

eighth_company = list(companiesfounders.keys())[7]
del companiesfounders[eighth_company]

last_key_value_pair_companies = list(companiesfounders.items())[-1]