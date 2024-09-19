companiesceos = {
    "Microsoft": "Satya Nadella",
    "Apple": "Tim Cook",
    "Amazon": "Andy Jassy",
    "Tesla": "Elon Musk",
    "Meta": "Mark Zuckerberg",
    "Alphabet": "Sundar Pichai",
    "IBM": "Arvind Krishna",
    "Oracle": "Safra Catz",
    "Disney": "Bob Iger",
    "Netflix": "Ted Sarandos"
}

entire_dict_companies = companiesceos

sixth_company = list(companiesceos.keys())[5]
sixth_company_ceo = companiesceos[sixth_company]

third_company = list(companiesceos.keys())[2]
companiesceos[third_company] = "Updated CEO"

ninth_company = list(companiesceos.keys())[8]
del companiesceos[ninth_company]

last_key_value_pair_companies = list(companiesceos.items())[-1]